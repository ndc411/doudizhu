from enum import IntEnum


class Protocol(IntEnum):

    ERROR = 0

    REQ_ROOM_LIST = 1001
    RSP_ROOM_LIST = 1002

    REQ_NEW_ROOM = 1003
    RSP_NEW_ROOM = 1004

    REQ_JOIN_ROOM = 1005
    RSP_JOIN_ROOM = 1006

    REQ_LEAVE_ROOM = 1007
    RSP_LEAVE_ROOM = 1008

    REQ_READY = 2001
    RSP_READY = 2002

    RSP_DEAL_POKER = 2004

    REQ_CALL_SCORE = 2005
    RSP_CALL_SCORE = 2006

    REQ_SHOT_POKER = 3001
    RSP_SHOT_POKER = 3002

    RSP_GAME_OVER = 4002

