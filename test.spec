Name:		test
Version:	2.1
Release:	1%{?dist}
Summary:	Dummy package for testing
Group:		System Environment/Base
License:	MIT
URL:		about:blank
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
This package does nothing. It is a dummy package used for testing.

Here is an extended test for UTF-8 characters:

    Sîne klâwen durh die wolken sint geslagen,
    er stîget ûf mit grôzer kraft,
    ich sih in grâwen tägelîch als er wil tagen,
    den tac, der im geselleschaft
    erwenden wil, dem werden man,
    den ich mit sorgen în verliez.
    ich bringe in hinnen, ob ich kan.
    sîn vil manegiu tugent michz leisten hiez.

    Tamil: நான் கண்ணாடி சாப்பிடுவேன், அதனால் எனக்கு ஒரு கேடும் வராது.
    Telugu: నేను గాజు తినగలను మరియు అలా చేసినా నాకు ఏమి ఇబ్బంది లేదు
    Sinhalese: මට වීදුරු කෑමට හැකියි. එයින් මට කිසි හානියක් සිදු නොවේ.
    Pashto(3): زه شيشه خوړلې شم، هغه ما نه خوږوي
    Farsi / Persian(3): .من می توانم بدونِ احساس درد شيشه بخورم
    Arabic(3): أنا قادر على أكل الزجاج و هذا لا يؤلمني.
    Aramaic: (NEEDED)
    Maltese: Nista' niekol il-ħġieġ u ma jagħmilli xejn.
    Twi: Metumi awe tumpan, ɜnyɜ me hwee.
    Hausa (Latin): Inā iya taunar gilāshi kuma in gamā lāfiyā.
    Hausa (Ajami) (2): إِنا إِىَ تَونَر غِلَاشِ كُمَ إِن غَمَا لَافِىَا
    Yoruba(4): Mo lè je̩ dígí, kò ní pa mí lára.
    Lingala: Nakokí kolíya biténi bya milungi, ekosála ngáí mabé tɛ́.
    (Ki)Swahili: Naweza kula bilauri na sikunyui.
    Malay: Saya boleh makan kaca dan ia tidak mencederakan saya.
    Tagalog: Kaya kong kumain nang bubog at hindi ako masaktan. 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)

%changelog
* Wed Jan 07 2015 Sakib Jalal <sfj19@nbcs.rutgers.edu> - 2.1-2.ru6
- First solaris9 Rutgers build
