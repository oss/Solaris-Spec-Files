%include perl-header.spec

Summary: Perl vacation script compatible with qmail
Name: qmail-vacation
Version: 1.4
Release: 2ru
Group: Applications/Internet
License: RU
Source: http://www.gormand.com.au/peters/tools/qmail/qmail-vacation-1.4.tar.gz
Patch: qmail-vacation-ru.patch
BuildRoot: /var/tmp/%{name}-root

Requires: perl qmail
Conflicts: vacation
Obsoletes: vacation-perl+qmail

%description
Perl vacation script that works with qmail.

%prep
%setup -q
chmod 644 *
%patch -p1

%build
#mv Makefile.dist Makefile
echo "VACATION = /usr/local/bin/vacation
PERL = %{perl_binary}
MAILPROG = /usr/local/qmail/bin/datemail -t" > Makefile
cat Makefile.dist >> Makefile
#sed "s/VACATION/#VACATION/" Makefile.dist > Makefile.tmp
#sed "s/PERL/#PERL/" Makefile.tmp > Makefile.dist
#sed "s/MAILPROG/#MAILPROG/" Makefile.dist >> Makefile
make


%install
mkdir -p %{buildroot}/usr/local/bin/ %{buildroot}/usr/local/man/man1/
cp vacation %{buildroot}/usr/local/bin/
cp vacation.1 %{buildroot}/usr/local/man/man1/

%clean
rm -rf %{buildroot}

%post
cat<<EOF
You may wish to> ln -s /usr/local/bin/vacation /usr/bin/vacation
EOF


%files
%defattr(0755,root,other) 
/usr/local/bin/vacation
%defattr(0644,root,other) 
/usr/local/man/man1/vacation.1




