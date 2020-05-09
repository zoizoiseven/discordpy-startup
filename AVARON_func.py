import discord
import random

# ステータス管理用変数
# ロール管理用クラス
class Role():
    ROLE_LIST = []

    role_list_name          =   0
    role_list_state         =   1

    isMerlin                =   0   # マーリン
    isPercival              =   1   # パーシバル
    isAssassin              =   2   # 暗殺者
    isMorgana               =   3   # モルガナ
    isMordred               =   4   # モードレッド
    isOberon                =   5   # オベロン

    ROLE_ID_LIST    =       list(range(6))

    def init_ROLE_LIST(self):
        self.ROLE_LIST   =   [   ['マーリン',       True],  \
                                ['パーシバル',      False],  \
                                ['暗殺者',          True],  \
                                ['モルガナ',        False], \
                                ['モードレッド',    False], \
                                ['オベロン',        False]  ]
        return
    def check_ROLELIST(self):
        if not Role.ROLE_LIST:
            self.init_ROLE_LIST()
        return

    # 役職設定用関数
    def role_set(self, role_id):
        self.ROLE_LIST[role_id][self.role_list_state] = True
        msg = self.ROLE_LIST[role_id][self.role_list_name] + 'が追加されました\n'
        return msg

    def role_del(self, role_id):
        self.ROLE_LIST[role_id][self.role_list_state] = False
        msg = self.ROLE_LIST[role_id][self.role_list_name] + 'を抜きました\n'
        return msg

    def role_switch(self, role_id):
        if self.ROLE_LIST[role_id][self.role_list_state] != True:
            msg = self.role_set()
        else:
            msg = self.role_del()
        return msg

    # 役職通知メッセージ作成関数
    def set_msg_Merlin(self):
        Merlin_msg_member = Player.role_Assassin + Player.role_Morgana + Player.role_Oberon + Player.role_evil
        random.shuffle(Merlin_msg_member)
        msg = "陣営は正義\n"
        msg += "役職はマーリンです\n"
        msg += "邪悪陣営は\n"
        for member in Merlin_msg_member:
            msg += member.name
            msg += "\n"
        msg += "です"
        return msg

    def set_msg_Percival(self):
        Percival_msg_member = Player.role_Merlin + Player.role_Morgana
        random.shuffle(Percival_msg_member)
        msg = "陣営は正義\n"
        msg += "役職はパーシバルです\n"
        msg += "マーリンは\n"
        for member in Percival_msg_member:
            msg += member.name
            msg += "\n"
        msg += "です"
        return msg

    def set_msg_justice(self):
        msg = "陣営は正義\n"
        msg += "役職は戦士(市民)です\n"
        return msg

    def set_msg_Assassin(self):
        msg = "陣営は邪悪\n"
        msg += "役職は暗殺者です\n"
        msg += "邪悪陣営は\n"
        for member in Player.role_evil_omit_Oberon:
            msg += member.name
            msg += "\n"
        msg += "です"
        return msg

    def set_msg_Morgana(self):
        msg = "陣営は邪悪\n"
        msg += "役職はモルガナです\n"
        msg += "邪悪陣営は\n"
        for member in Player.role_evil_omit_Oberon:
            msg += member.name
            msg += "\n"
        msg += "です"
        return msg

    def set_msg_Mordred(self):
        msg = "陣営は邪悪\n"
        msg += "役職はモードレッドです\n"
        msg += "邪悪陣営は\n"
        for member in Player.role_evil_omit_Oberon:
            msg += member.name
            msg += "\n"
        msg += "です"
        return msg

    def set_msg_Oberon(self):
        msg = "陣営は邪悪\n"
        msg += "役職はオベロンです\n"
        return msg

    def set_msg_evil(self):
        msg = "陣営は邪悪\n"
        msg += "役職は戦士(一般)です\n"
        msg += "邪悪陣営は\n"
        for member in Player.role_evil_omit_Oberon:
            msg += member.name
            msg += "\n"
        msg += "です"
        return msg

# 状態管理用クラス
class Status():
    Status_msg              =   ""
    GAME_STATUS             =   0   
    isDefault               =   0   # default状態
    isSetuping              =   1   # セットアップ中フラグ
    isWaitingGameStart      =   2   # 試合開始待ちフラグ
    isWaitingVote           =   3   # 投票待ちフラグ
    isVoting                =   4   # 投票中フラグ
    isWaitingQuest          =   5   # クエスト開始待ちフラグ
    isQuesting              =   6   # クエスト結果待ちフラグ
    isWaitingResult         =   7   # ゲーム結果待ちフラグ


    def update_status_isDefault(self):
        self.GAME_STATUS    =   self.isDefault
        self.Status_msg     =   ""
        return
    def update_status_isSetuping(self):
        self.GAME_STATUS    =   self.isSetuping
        self.Status_msg     =   "参加受付"
        return
    def update_status_isWaitingGameStart(self):
        self.GAME_STATUS    =   self.isWaitingGameStart
        self.Status_msg     =   "準備完了"
        return
    def update_status_isWaitingVote(self):
        self.GAME_STATUS    =   self.isWaitingVote
        self.Status_msg     =   "チーム編成待ち"
        return
    def update_status_isVoting(self):
        self.GAME_STATUS    =   self.isVoting
        self.Status_msg     =   "チーム編成投票中"
        return
    def update_status_isWaitingQuest(self):
        self.GAME_STATUS    =   self.isWaitingQuest
        self.Status_msg     =   "クエスト開始待ち"
        return
    def update_status_isQuesting(self):
        self.GAME_STATUS    =   self.isQuesting
        self.Status_msg     =   "クエスト投票中"
        return
    def update_status_isWaitingResult(self):
        self.GAME_STATUS    =   self.isWaitingResult
        self.Status_msg     =   "暗殺投票待ち"
        return
    def get_status(self):
        return self.GAME_STATUS
    def set_status_msg(self):
        if self.GAME_STATUS == self.isWaitingVote:
            msg = "クエストに行くメンバーを" + str(Quest.quest_member_num) + "人指定し、「/提案 @name」と送信してください"
        elif self.GAME_STATUS == self.isWaitingQuest:
            msg = "「/クエスト」と送信してください"
        elif self.GAME_STATUS == self.isWaitingResult:
            msg = "マーリンだと思う人を指定し、「/暗殺　@name」と送信してください"
        else:
            msg = ""
        return msg

    # ゲーム情報表示用関数
    def get_game_status(self):
        msg = "【参加人数】"
        msg += str(Player.player_number)
        msg += "人：\n"
        msg += "正義陣営："
        justice = Player.PLAYERNUM_JUSTICE_LIST[Player.player_number - 5]
        msg += str(justice)
        msg += "人\n"
        msg += "邪悪陣営："
        evil = Player.player_number - Player.PLAYERNUM_JUSTICE_LIST[Player.player_number - 5]
        msg += str(evil)
        msg += "人\n"
        role = [role_list[Role.role_list_name] for role_list in Role.ROLE_LIST if role_list[Role.role_list_state] == True]
        msg += '【役職】\n'
        for role_name in role:
            msg += role_name
            msg += "\n"
        msg += "【参加者】\n"
        for member in Player.player_member_list:
            msg += member.name
            msg += "\n"
        msg += "クエスト参加人数："
        msg += str(Quest.QUEST_MEM_LIST[Player.player_number - 5])
        msg += "\n"
        msg += "失敗条件(枚数)："
        msg += str(Quest.QUEST_FAILURE_LIST[Player.player_number - 5])
        msg += "\n"
        return msg
   

# 投票用クラス
class Vote():
    quest_member_list   =   []  # 指名されたメンバーのリスト
    VOTE_LIST           =   []  # 投票者名、結果
    vote_total_num      =   0   # 投票数合計
    vote_agree_num      =   0   # 賛成票合計
    vote_against_num    =   0   # 反対票合計

    def init_vote_setup(self):
        self.quest_member_list   =   []  # 指名されたメンバーのリスト
        self.VOTE_LIST           =   []  # 投票者名、結果
        self.vote_total_num      =   0   # 投票数合計
        self.vote_agree_num      =   0   # 賛成票合計
        self.vote_against_num    =   0   # 反対票合計
        return

    def init_vote_start(self):
        self.quest_member_list   =   []  # 指名されたメンバーのリスト
        self.VOTE_LIST           =   []  # 投票者名、結果
        self.vote_total_num      =   0   # 投票数合計
        self.vote_agree_num      =   0   # 賛成票合計
        self.vote_against_num    =   0   # 反対票合計
        return

    def init_vote_continue(self):
        self.quest_member_list   =   []  # 指名されたメンバーのリスト
        self.VOTE_LIST           =   []  # 投票者名、結果
        self.vote_total_num      =   0   # 投票数合計
        self.vote_agree_num      =   0   # 賛成票合計
        self.vote_against_num    =   0   # 反対票合計
        return

    def init_vote_end(self):
        self.VOTE_LIST           =   []  # 投票者名、結果
        self.vote_total_num      =   0   # 投票数合計
        self.vote_agree_num      =   0   # 賛成票合計
        self.vote_against_num    =   0   # 反対票合計
        return

    def update_vote_agree(self, name):
        tmp_vote_result       =   name + "\t賛成\n"
        self.VOTE_LIST.append(tmp_vote_result)
        self.vote_total_num      +=  1
        self.vote_agree_num      +=  1
        msg = "投票を受け付けました"
        return msg

    def update_vote_against(self, name):
        tmp_vote_result       =   name + "\t反対\n"
        self.VOTE_LIST.append(tmp_vote_result)
        self.vote_total_num      +=  1
        self.vote_against_num      +=  1
        msg = "投票を受け付けました"
        return msg

    def set_vote_msg(self):
        msg = "【投票完了：" + str(Result.vote_total_num + 1) + "回目】\n"
        if self.vote_agree_num < self.vote_against_num:
            msg += "結果：否決\n"
        else:
            msg += "結果：可決\n"
        msg += "賛成："
        msg += str(self.vote_agree_num)
        msg += "\n"
        msg += "反対："
        msg += str(self.vote_against_num)
        msg += "\n"
        msg += "【内訳】\n"
        for result_msg in self.VOTE_LIST:
            msg += result_msg
        return msg

# クエスト用クラス
class Quest():
    quest_vote_member         =   []
    quest_member_num        =   0
    quest_round             =   1
    quest_vote_num          =   0
    quest_failure_num       =   0

    quest_result_status     =   0
    quest_default_status    =   0
    quest_result_success    =   1
    quest_result_failure    =   2

    quest_round_list        =   list(range(5))
    QUEST_MEM_LIST          =   (   (2, 3, 2, 3, 3),    \
                                    (2, 3, 4, 3, 4),    \
                                    (2, 3, 3, 4, 4),    \
                                    (3, 4, 4, 5, 5),    \
                                    (3, 4, 4, 5, 5),    \
                                    (3, 4, 4, 5, 5)     )
    QUEST_FAILURE_LIST      =   (   (1, 1, 1, 1, 1),    \
                                    (1, 1, 1, 1, 1),    \
                                    (1, 1, 1, 2, 1),    \
                                    (1, 1, 1, 2, 1),    \
                                    (1, 1, 1, 2, 1),    \
                                    (1, 1, 1, 2, 1)     )
    def init_setup(self):
        self.quest_vote_member         =   []
        self.quest_round             =   1
        self.quest_vote_num          =   0
        self.quest_failure_num       =   0
        self.quest_result_status     =   self.quest_default_status
        self.update_quest_member_num()
        return

    def init_quest_start(self):
        self.quest_vote_member         =   []
        self.quest_vote_num          =   0
        self.quest_failure_num       =   0
        self.update_quest_member_num()
        return
    
    def update_quest_success(self, member):
        self.quest_vote_member.append(member)
        self.quest_vote_num          +=   1
        msg = "投票を受け付けました"
        return msg
    
    def update_quest_failure(self, member):
        self.quest_vote_member.append(member)
        self.quest_vote_num          +=   1
        self.quest_failure_num       +=   1
        msg = "投票を受け付けました"
        return msg

    def update_quest_result(self):
        if self.quest_failure_num < self.QUEST_FAILURE_LIST[Player.player_number - 5][self.quest_round - 1]:
            self.quest_result_status     =   self.quest_result_success
        else:
            self.quest_result_status     =   self.quest_result_failure
        return
    
    def init_quest_end(self):
        self.quest_vote_member         =   []
        self.quest_round             +=   1
        self.quest_vote_num          =   0
        self.quest_failure_num       =   0
        self.quest_result_status     =   self.quest_default_status
        self.update_quest_member_num()
        return
    
    def update_quest_member_num(self):
        if self.quest_round <= 5:
            self.quest_member_num = self.QUEST_MEM_LIST[Player.player_number - 5][self.quest_round - 1]
        return

    def set_quest_msg(self):
        msg = "【投票完了：" + str(self.quest_round) + "回目】\n"
        msg += self.get_quest_result_msg()
        msg += self.get_quest_member_msg()
        return msg

    def get_quest_result_msg(self):
        self.update_quest_result()
        if self.quest_result_status == self.quest_result_success:
            msg = "結果：成功\n"
        else:
            msg = "結果：失敗\n"
        msg += "失敗："
        msg += str(self.quest_failure_num)
        msg += "票\n"
        return msg

    def get_quest_member_msg(self):
        msg = "投票メンバー\n"
        for member in self.quest_vote_member:
            msg += member.name
            msg += "\t"
        msg += "\n"
        return msg
 

# プレイヤー用クラス
class Player():
    PLAYERNUM_JUSTICE_LIST  =   (3, 4, 4, 5, 6, 6) # 5~10人
    player_number           =   5
    player_member_list      =   []   # 参加者のリスト
    player_justice_list     =   []   # 参加者(正義)のリスト
    player_evil_list        =   []   # 参加者(邪悪)のリスト
    role_Merlin    =   []
    role_Percival  =   []
    role_justice   =   []
    role_Assassin  =   []
    role_Morgana   =   []
    role_Mordred   =   []
    role_Oberon    =   []
    role_evil      =   []
    role_evil_omit_Oberon      =   []

    def init_player(self):
        self.player_number           =   5
        self.player_member_list      =   []   # 参加者のリスト
        self.player_justice_list     =   []   # 参加者(正義)のリスト
        self.player_evil_list        =   []   # 参加者(邪悪)のリスト
        self.role_Merlin    =   []
        self.role_Percival  =   []
        self.role_justice   =   []
        self.role_Assassin  =   []
        self.role_Morgana   =   []
        self.role_Mordred   =   []
        self.role_Oberon    =   []
        self.role_evil      =   []
        self.role_evil_omit_Oberon      =   []
        return
    
    def update_player_number(self):
        self.player_number = len(self.player_member_list)
        return

    # 配役用関数
    def role_cast(self):
        # プレイヤーのリストをソート
        random.shuffle(self.player_member_list)
        # 正義陣営と邪悪陣営に分割
        for member in self.player_member_list:
            if len(self.player_justice_list) < self.PLAYERNUM_JUSTICE_LIST[self.player_number - 5]:
                self.player_justice_list.append(member)
            else:
                self.player_evil_list.append(member)
        # 正義陣営の役職を割り振る
        for member in self.player_justice_list:
            if len(self.role_Merlin) < Role.ROLE_LIST[Role.isMerlin][Role.role_list_state]:
                self.role_Merlin.append(member)
            elif len(self.role_Percival) < Role.ROLE_LIST[Role.isPercival][Role.role_list_state]:
                self.role_Percival.append(member)
            else:
                self.role_justice.append(member)
        # 邪悪陣営の役職を割り振る
        for member in self.player_evil_list:
            if len(self.role_Assassin) < Role.ROLE_LIST[Role.isAssassin][Role.role_list_state]:
                self.role_Assassin.append(member)
            elif len(self.role_Morgana) < Role.ROLE_LIST[Role.isMorgana][Role.role_list_state]:
                self.role_Morgana.append(member)
            elif len(self.role_Mordred) < Role.ROLE_LIST[Role.isMordred][Role.role_list_state]:
                self.role_Mordred.append(member)
            elif len(self.role_Oberon) < Role.ROLE_LIST[Role.isOberon][Role.role_list_state]:
                self.role_Oberon.append(member)
            else:
                self.role_evil.append(member)
        # 示し合わせのできる邪悪リスト作成
        tmp_evil_list = self.role_Assassin + self.role_Morgana + self.role_Mordred + self.role_evil
        random.shuffle(tmp_evil_list)
        for member in tmp_evil_list:
            self.role_evil_omit_Oberon.append(member)
        random.shuffle(self.player_member_list)
        return

# 結果判定用クラス
class Result():
    vote_limit              =   5
    quest_failure_limit     =   3
    quest_seccess_limit     =   3

    vote_total_num          =   0
    quest_failure_total     =   0
    quest_success_total     =   0

    game_result             =   0
    default                 =   0
    win_justice             =   1
    win_evil                =   2

    def init_result(self):
        self.vote_total_num          =   0
        self.quest_failure_total     =   0
        self.quest_success_total     =   0
        self.game_result             =   self.default
        return

    def update_vote_total_num(self):
        self.vote_total_num         +=  1
        if self.vote_total_num >= self.vote_limit:
            self.game_result        =   self.win_evil
        return

    def update_quest_result(self):
        if Quest.quest_result_status == Quest.quest_result_success:
            self.quest_success_total         +=  1
            if self.quest_success_total >= self.quest_seccess_limit:
                self.game_result    =   self.win_justice
        else:
            self.quest_failure_total         +=  1
            if self.quest_failure_total >= self.quest_failure_limit:
                self.game_result    =   self.win_evil
        return

    def set_game_result_msg(self):
        if self.game_result == self.win_justice:
            msg = "正義陣営の勝利です\n"
        else:
            msg = "邪悪陣営の勝利です\n"
        msg += "【役職】\n"
        for member in Player.role_Merlin:
            msg += "マーリン：\t"
            msg += member.name
            msg += "\n"
        for member in Player.role_Percival:
            msg += "パーシバル：\t"
            msg += member.name
            msg += "\n"
        for member in Player.role_justice:
            msg += "市民：\t"
            msg += member.name
            msg += "\n"
        for member in Player.role_Assassin:
            msg += "暗殺者：\t"
            msg += member.name
            msg += "\n"
        for member in Player.role_Morgana:
            msg += "モルガナ：\t"
            msg += member.name
            msg += "\n"
        for member in Player.role_Mordred:
            msg += "モードレッド：\t"
            msg += member.name
            msg += "\n"
        for member in Player.role_Oberon:
            msg += "オベロン：\t"
            msg += member.name
            msg += "\n"
        for member in Player.role_evil:
            msg += "邪悪：\t"
            msg += member.name
            msg += "\n"
        return msg

# インスタンス作成
Role = Role()
Status = Status()
Vote = Vote()
Quest = Quest()
Player = Player()
Result = Result()

# 初期化関数
# 参加者受付開始
def avaron_setupinit():
    Status.update_status_isSetuping()
    Player.init_player()
    Result.init_result()
    Vote.init_vote_setup()
    return
# 参加者受付完了
def avaron_setupendinit():
    Status.update_status_isWaitingGameStart()
    Player.update_player_number()
    Role.check_ROLELIST()
    return

# ゲーム開始時
def avaron_startinit():
    Status.update_status_isWaitingVote()
    Quest.init_setup()
    Vote.init_vote_setup()
    return

# チーム編成投票開始時
def avaron_voteinit():
    Status.update_status_isVoting()
    Vote.init_vote_start()
    return
# チーム編成投票否決
def avaron_votecontinit():
    Status.update_status_isWaitingVote()
    Vote.init_vote_continue()
    Result.update_vote_total_num()
    return
# チーム編成投票可決
def avaron_voteendinit():
    Status.update_status_isWaitingQuest()
    Vote.init_vote_end()
    return

# クエスト投票開始
def avaron_questinit():
    Status.update_status_isQuesting()
    Quest.init_quest_start()
    return
# クエスト投票終了
def avaron_questendinit():
    Status.update_status_isWaitingVote()
    Result.update_quest_result()
    Quest.init_quest_end()
    return

# ゲーム終了時
def avaron_endinit():
    Status.update_status_isDefault()
    Player.init_player()
    Role.init_ROLE_LIST()
    Vote.init_vote_setup()
    Quest.init_setup()
    Result.init_result()
    return
        
        
