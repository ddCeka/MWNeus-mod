#Character
#player
default firstname = "Neron"
default persistent.gallery_firstname = "Neron"
define mc = Character('[firstname]', color="#4948FF")
#neus
default neusname = "Neus"
default persistent.gallery_neusname = "Neus"
default neusname_yan = "???"
default neusname_lyra = "Lyra"
default persistent.gallery_lyra = "Lyra"
default neusname_ny = "???"
default neusname_sylvia = "Sylvia"
default persistent.gallery_sylvia = "Sylvia"
default momname = "Mother of " + neusname
define neus = Character('[neusname]', color="#FE2EF7")
define neus_yan = Character('[neusname_yan]', color="#760272")
define neus_lyra = Character('[neusname_lyra]', color="#760272")
define neus_lyra_neus = Character('[neusname] & [neusname_lyra]', color="#FE2EF7")
define neus_ny = Character('[neusname_ny]', color="#a91160")
define neus_sylvia = Character('[neusname_sylvia]', color="#a91160")
define ly_ne_ny = Character('[neusname] & [neusname_lyra] & [neusname_ny]', color="#FE2EF7")
define ly_ne_syl = Character('[neusname] & [neusname_lyra] & [neusname_sylvia]', color="#FE2EF7")
define ly_syl = Character('[neusname_lyra] & [neusname_sylvia]', color="#FE2EF7")
define ne_syl = Character('[neusname] & [neusname_sylvia]', color="#FE2EF7")
#extra
define waitress = Character(_('Waitress'), color="#2a5232")
define manager = Character(_('Manager'), color="#2a3d2e")
define recep = Character(_('Receptionist'), color="#2a5232")
define swoman = Character(_('Saleswoman'), color="#2a5232")
define rcouples = Character(_('Random couples'), color="#2a5232")
define mom_n = Character(_('[momname]'), color="#1318a5")
define girl1 = Character(_('Girl1'), color="#ff0000")
define girl2 = Character(_('Girl2'), color="#000000")
define girl3 = Character(_('Girl3'), color="#fffb00")
define granddaughter = Character(_('Granddaughter'), color="#0e314e")
define strange_woman = Character(_('Strange Woman'), color="#ba8a12")