import discord
import os
from discord.ext import commands
from AVARON_func import *

bot = commands.Bot(command_prefix='/') 
token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = 706355172301078577
STATUS_CHANNEL_ID = 707196746824024074

@bot.event
async def on_ready():
    """起動時に通知してくれる処理"""
    print('ログインしました')

# 参加者受付開始
@bot.command(aliases=['参加受付'])
async def setup_avaron(ctx):
    if Status.get_status() == Status.isDefault or Status.get_status() == Status.isWaitingGameStart:
        # status初期化
        avaron_setupinit()
        await bot.change_presence(activity=discord.Game(Status.Status_msg))
        msg = '参加者は「/参加」と発言してください\n受付終了時は「/締め」と入力してください'
    else:
        msg = "今は無効なコマンドです"
    await ctx.channel.send(msg)

# 参加者受付
@bot.command(aliases=['参加'])
async def add_avaron(ctx):
    if Status.get_status() == Status.isSetuping:
        # 同じ名前の人は弾く
        Player.player_member_list.append(ctx.author)
        await ctx.channel.send(ctx.author.name + "さんの参加を受付ました：" + str(len(Player.player_member_list)) + "人目")
    else:
        await ctx.channel.send("参加受付のためには「/参加受付」を入力")

# 参加者受付終了
@bot.command(aliases=['締め'])
async def setup_end_avaron(ctx):
    if Status.get_status() == Status.isSetuping:
        avaron_setupendinit()
        await bot.change_presence(activity=discord.Game(Status.Status_msg))
        msg = "【参加者】" + "\n"
        member_name_list = [member.name for member in Player.player_member_list]
        for name in member_name_list:
            msg += name
            msg += "\n"
    else:
        msg = "受付開始のためには「/参加受付」を入力"
    msg += "ゲーム開始のためには「/ゲーム開始」を入力"
    await ctx.channel.send(msg)

# アヴァロン開始
@bot.command(aliases=['ゲーム開始'])
async def start_avaron(ctx):
    if Status.get_status() == Status.isWaitingGameStart:
        # status初期化
        avaron_startinit()
        await bot.change_presence(activity=discord.Game(Status.Status_msg))
        # 役職分配
        Player.role_cast()
        # 個人にDM(役職)
        for member in Player.role_Merlin:
            dm = member.dm_channel
            if dm == None:
                dm = await member.create_dm()
            msg = member.name + "さんの"
            msg += Role.set_msg_Merlin()
            await dm.send(msg)
        for member in Player.role_Percival:
            dm = member.dm_channel
            if dm == None:
                dm = await member.create_dm()
            msg = member.name + "さんの"
            msg += Role.set_msg_Percival()
            await dm.send(msg)
        for member in Player.role_justice:
            dm = member.dm_channel
            if dm == None:
                dm = await member.create_dm()
            msg = member.name + "さんの"
            msg += Role.set_msg_justice()
            await dm.send(msg)
        for member in Player.role_evil:
            dm = member.dm_channel
            if dm == None:
                dm = await member.create_dm()
            msg = member.name + "さんの"
            msg += Role.set_msg_evil()
            await dm.send(msg)
        for member in Player.role_Morgana:
            dm = member.dm_channel
            if dm == None:
                dm = await member.create_dm()
            dm = member.dm_channel
            msg = member.name + "さんの"
            msg += Role.set_msg_Morgana()
            await dm.send(msg)
        for member in Player.role_Assassin:
            dm = member.dm_channel
            if dm == None:
                dm = await member.create_dm()
            msg = member.name + "さんの"
            msg += Role.set_msg_Assassin()
            await dm.send(msg)
        for member in Player.role_Mordred:
            dm = member.dm_channel
            if dm == None:
                dm = await member.create_dm()
            msg = member.name + "さんの"
            msg += Role.set_msg_Mordred()
            await dm.send(msg)
        for member in Player.role_Oberon:
            dm = member.dm_channel
            if dm == None:
                dm = await member.create_dm()
            msg = member.name + "さんの"
            msg += Role.set_msg_Oberon()
            await dm.send(msg)
        msg = Role.get_role_status()
        msg += '\nDMのメッセージを確認し、ゲームを始めてください\n'
        msg += Status.set_status_msg()
    else:
        msg = "「/参加受付」で参加者を設定してください"
    # 通知
    await ctx.channel.send(msg)

# 提案開始
@bot.command(aliases=['提案'])
async def vote_start(ctx, *args: discord.Member):
    if Status.get_status() == Status.isWaitingVote:
        if len(args) == Quest.quest_member_num:
            avaron_voteinit()
            await bot.change_presence(activity=discord.Game(Status.Status_msg))
            msg = "提案者：" + ctx.author.name + "\n"
            msg += "【メンバー】\n"
            for vote_member in args:
                if len(Vote.quest_member_list) < Quest.quest_member_num:
                    Vote.quest_member_list.append(vote_member)
                    msg += vote_member.name
                    msg += "\t"
            msg += "\n"
            msg += "プレイヤーはDMで「/編成投票　賛成」「/編成投票　反対」を送信してください\n"
            for member in Player.player_member_list:
                dm = member.dm_channel
                if dm == None:
                    dm = await member.create_dm()
                await dm.send(msg)
        else:
            msg = "このラウンドでは" + str(Quest.quest_member_num) + "人指定してください"
    else:
        msg = "今は無効なコマンドです"
    await ctx.channel.send(msg)

# 提案投票
@bot.command(aliases=['編成投票'])
@commands.dm_only()
async def vote_vote(ctx, args):
    if Status.get_status() == Status.isVoting:
        if args == "賛成":
            msg = Vote.update_vote_agree(ctx.author.name)
        elif args == "反対":
            msg = Vote.update_vote_against(ctx.author.name)
        else:
            msg = "「/投票 成功」または「/投票 失敗」と送信してください"
        await ctx.channel.send(msg)
        # 投票数が規定数に達した場合、結果を規定Channelに送信
        if Vote.vote_total_num >= Player.player_number:
            msg = Vote.set_vote_msg()
            channel = bot.get_channel(CHANNEL_ID)
            if Vote.vote_agree_num >= Vote.vote_against_num:
                avaron_voteendinit()
            else:
                avaron_votecontinit()
            await bot.change_presence(activity=discord.Game(Status.Status_msg))
            msg += Status.set_status_msg()
            await channel.send(msg)
    else:
        msg = "今は無効なコマンドです"
        await ctx.channel.send(msg)
    # ゲーム終了判定
    if Result.game_result == Result.win_evil:
        msg = Result.set_game_result_msg()
        await channel.send(msg)
        avaron_endinit()
        await bot.change_presence(activity=discord.Game(""))

# クエスト開始
@bot.command(aliases=['クエスト'])
async def quest_start(ctx):
    if Status.get_status() == Status.isWaitingQuest:
        avaron_questinit()
        await bot.change_presence(activity=discord.Game(Status.Status_msg))
        msg = str(Quest.quest_round) + "回目のメンバーは\n"
        for quest_member in Vote.quest_member_list:
            dm = quest_member.dm_channel
            if dm == None:
                dm = await quest_member.create_dm()
            dm_msg = "「/投票 成功」または「/投票 失敗」と送信してください"
            await dm.send(dm_msg)
            msg += quest_member.name
            msg += "\n"
        msg += "です\n"
        msg += "DMに「/投票 成功」または「/投票 失敗」と送信してください"
    else:
        msg = "今は無効なコマンドです"
    await ctx.channel.send(msg)

# クエスト投票
@bot.command(aliases=['投票'])
@commands.dm_only()
async def quest_vote(ctx, args):
    if Status.get_status() == Status.isQuesting:
        if args == "成功":
            msg = Quest.update_quest_success(ctx.author)
        elif args == "失敗":
            msg = Quest.update_quest_failure(ctx.author)
        else:
            msg = "「/投票 成功」または「/投票 失敗」と送信してください"
        await ctx.channel.send(msg)
        # 投票数が規定数に達した場合、結果を規定Channelに送信
        if Quest.quest_vote_num >= Quest.quest_member_num:
            await bot.change_presence(activity=discord.Game(Status.Status_msg))
            channel = bot.get_channel(CHANNEL_ID)
            msg = Quest.set_quest_msg()
            avaron_questendinit()
            msg += Status.set_status_msg()
            await channel.send(msg)
    else:
        msg = "今は無効なコマンドです"
        await ctx.channel.send(msg)
    # ゲーム終了判定
    if Result.game_result != Result.default:
        if Result.game_result == Result.win_evil:
            msg = Result.set_game_result_msg()
            await channel.send(msg)
            avaron_endinit()
            await bot.change_presence(activity=discord.Game(""))
        else:
            msg = "クエストに" + str(Result.quest_success_total) + "回成功しました\n"
            Status.update_status_isWaitingResult()
            msg += Status.set_status_msg()
            await channel.send(msg)

                
# 暗殺
@bot.command(aliases=['暗殺'])
async def assassinate_avaron(ctx, member: discord.Member):
    channel = bot.get_channel(CHANNEL_ID)
    if member == Player.role_Merlin[0]:
        Result.game_result = Result.win_evil
        msg = Result.set_game_result_msg()
    else:
        msg = Result.set_game_result_msg()
    await channel.send(msg)
    avaron_endinit()
    await bot.change_presence(activity=discord.Game(""))
        
# アヴァロン終了
@bot.command(aliases=['end'])
async def end_avaron(ctx):
    # status初期化
    avaron_endinit()
    await bot.change_presence(activity=discord.Game(""))
    await ctx.channel.send('ゲームエンド')

# 役職選択
@bot.command(aliases=['役職設定'])
async def role_set(ctx, *args):
    if Status.get_status() == Status.isDefault or Status.get_status() == Status.isSetuping or Status.get_status() == Status.isWaitingGameStart:
        Role.init_ROLE_LIST()
        msg = ""
        for role_id in Role.ROLE_ID_LIST:
            if Role.ROLE_LIST[role_id][Role.role_list_name] in args:
                msg += Role.role_set(role_id)
        if msg == "":
            msg = "変更なし"
    else:
        msg = "役職の変更はゲーム中にはできません"
    await ctx.channel.send(msg)
    result = Role.get_role_status()
    await ctx.channel.send(result)

#役職確認
@bot.command(aliases=['ゲーム情報'])
async def show_status(ctx):
    if Status.get_status() != Status.isDefault and Status.get_status() != Status.isSetuping and Status.get_status() != Status.isWaitingGameStart:
        Role.check_ROLELIST()
        msg = Status.get_game_status()
        channel = bot.get_channel(STATUS_CHANNEL_ID)
        await channel.send(msg)

# bot切断(sakujo)
# @bot.command('再起動')
# async def bye_reboot(ctx):
#    bot.clear()
#    bot.run(token)

# bot切断(sakujo)
# @bot.command()
# async def bye(ctx):
#    await bot.logout()
#    await sys.exit()

# botの接続と起動
# （botアカウントのアクセストークンを入れてください）
bot.run(token)
