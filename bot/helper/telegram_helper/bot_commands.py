#!/usr/bin/env python3
from bot import CMD_SUFFIX, config_dict

class _BotCommands:
    def __init__(self):
        self.StartCommand = 'start'
        self.MirrorCommand = [f'hinata{CMD_SUFFIX}', f'hin{CMD_SUFFIX}']
        self.QbMirrorCommand = [f'naruto{CMD_SUFFIX}', f'nar{CMD_SUFFIX}']
        self.YtdlCommand = [f'kakashi{CMD_SUFFIX}', f'kaka{CMD_SUFFIX}']
        self.LeechCommand = [f'upload{CMD_SUFFIX}', f'up{CMD_SUFFIX}']
        self.QbLeechCommand = [f'qbupload{CMD_SUFFIX}', f'qup{CMD_SUFFIX}']
        self.YtdlLeechCommand = [f'ytdlupload{CMD_SUFFIX}', f'yup{CMD_SUFFIX}']
        if config_dict['SHOW_EXTRA_CMDS']:
            self.MirrorCommand.extend([f'asdf{CMD_SUFFIX}', f'jks{CMD_SUFFIX}', f'ishu{CMD_SUFFIX}', f'is{CMD_SUFFIX}'])
            self.QbMirrorCommand.extend([f'jisku{CMD_SUFFIX}', f'esghu{CMD_SUFFIX}', f'sakuma{CMD_SUFFIX}', f'sak{CMD_SUFFIX}'])
            self.YtdlCommand.extend([f'sizuka{CMD_SUFFIX}', f'siz{CMD_SUFFIX}'])
            self.LeechCommand.extend([f'obitp{CMD_SUFFIX}', f'obt{CMD_SUFFIX}', f'mazara{CMD_SUFFIX}', f'dg{CMD_SUFFIX}'])
            self.QbLeechCommand.extend([f'gdhdj{CMD_SUFFIX}', f'shsh{CMD_SUFFIX}', f'sksjs{CMD_SUFFIX}', f'jisz{CMD_SUFFIX}'])
            self.YtdlLeechCommand.extend([f'jisksu{CMD_SUFFIX}', f'kjh{CMD_SUFFIX}'])
        self.CloneCommand = [f'madara{CMD_SUFFIX}', f'm{CMD_SUFFIX}']
        self.CountCommand = f'count{CMD_SUFFIX}'
        self.DeleteCommand = f'del{CMD_SUFFIX}'
        self.CancelMirror = f'cancel{CMD_SUFFIX}'
        self.CancelAllCommand = [f'cancelall{CMD_SUFFIX}', 'cancellallbot']
        self.ListCommand = f'jidhu{CMD_SUFFIX}'
        self.SearchCommand = f'search{CMD_SUFFIX}'
        self.StatusCommand = [f'status{CMD_SUFFIX}', f's{CMD_SUFFIX}', 'statusall']
        self.UsersCommand = f'users{CMD_SUFFIX}'
        self.AuthorizeCommand = [f'authorize{CMD_SUFFIX}', f'a{CMD_SUFFIX}']
        self.UnAuthorizeCommand = [f'unauthorize{CMD_SUFFIX}', f'ua{CMD_SUFFIX}']
        self.AddBlackListCommand = [f'blacklist{CMD_SUFFIX}', f'bl{CMD_SUFFIX}']
        self.RmBlackListCommand = [f'rmblacklist{CMD_SUFFIX}', f'rbl{CMD_SUFFIX}']
        self.AddSudoCommand = f'addsudo{CMD_SUFFIX}'
        self.RmSudoCommand = f'rmsudo{CMD_SUFFIX}'
        self.PingCommand = [f'ping{CMD_SUFFIX}', f'p{CMD_SUFFIX}']
        self.RestartCommand = [f'restart{CMD_SUFFIX}', f'r{CMD_SUFFIX}', 'restartall']
        self.StatsCommand = [f'stats{CMD_SUFFIX}', f'st{CMD_SUFFIX}']
        self.HelpCommand = f'help{CMD_SUFFIX}'
        self.LogCommand = f'log{CMD_SUFFIX}'
        self.ShellCommand = f'shell{CMD_SUFFIX}'
        self.EvalCommand = f'eval{CMD_SUFFIX}'
        self.ExecCommand = f'exec{CMD_SUFFIX}'
        self.ClearLocalsCommand = f'clearzlocals{CMD_SUFFIX}'
        self.BotSetCommand = [f'bsetting{CMD_SUFFIX}', f'bs{CMD_SUFFIX}']
        self.UserSetCommand = [f'setting{CMD_SUFFIX}', f'set{CMD_SUFFIX}']
        self.BtSelectCommand = f'btzstz{CMD_SUFFIX}'
        self.CategorySelect = f'ctzszel{CMD_SUFFIX}'
        self.SpeedCommand = [f'speedtest{CMD_SUFFIX}', f'sp{CMD_SUFFIX}']
        self.RssCommand = f'rszs{CMD_SUFFIX}'
        self.LoginCommand = 'login'
        self.AddImageCommand = f'addimg{CMD_SUFFIX}'
        self.ImagesCommand = f'images{CMD_SUFFIX}'
        self.IMDBCommand = f'imdb{CMD_SUFFIX}'
        self.AniListCommand = f'anime{CMD_SUFFIX}'
        self.AnimeHelpCommand = f'animehelp{CMD_SUFFIX}'
        self.MediaInfoCommand = [f'mediainfo{CMD_SUFFIX}', f'mzi{CMD_SUFFIX}']
        self.MyDramaListCommand = f'mdl{CMD_SUFFIX}'
        self.GDCleanCommand = [f'gdzclean{CMD_SUFFIX}', f'gzc{CMD_SUFFIX}']
        self.BroadcastCommand = [f'broadcast{CMD_SUFFIX}', f'bc{CMD_SUFFIX}']

BotCommands = _BotCommands()
