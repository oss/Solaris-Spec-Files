Name: ispell
Version: 3.3.02
Copyright: GPL?
Group: Applications/Editors
Summary: Interactive spell-checker
Release: 1
Source: ispell-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

%description

Ispell is an interactive spell checker.  It can check spelling in
flat-text, TeX, and troff files, and it has hooks in emacs.

%prep
%setup -q -n ispell-%{version}
make local.h
echo "#define CC \"cc\"" >> local.h
echo "#define USG" >> local.h
echo "#define TERMLIB \"-lcurses\"" >> local.h
make all 

%build
PATH="/opt/SUNWspro/bin:/usr/local/lib:/usr/ccs/bin:/usr/ucb:/usr/local/gnu/bin:/usr/local/bin:$PATH %{buildroot}"
export PATH

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
mkdir $RPM_BUILD_ROOT/usr/local/info
mkdir $RPM_BUILD_ROOT/usr/local/lib
cp config.sh config.sh.bak
perl -p -e "s(/usr)($RPM_BUILD_ROOT/usr)" < config.sh.bak > config.sh
cd deformatters
chmod u+w Makefile
cp Makefile Makefile.wrong
perl -p -e 's(defmt-c: defmt-c.o)(defmt-c:); s(defmt-sh: defmt-sh.o)(defmt-sh:)'  < Makefile.wrong > Makefile
cd ..
make install
cd $RPM_BUILD_ROOT/usr/local/lib
for i in `find . -links +1 -type f`;
do
    cp $i $i-2
    mv -f $i-2 $i
done


%clean
rm -rf $RPM_BUILD_ROOT

#%post
#if [ -x /usr/local/bin/install-info ] ; then
#	/usr/local/bin/install-info --info-dir=/usr/local/info \
#--entry="* Ispell: (ispell).                Interactive spell-checker" \
#		 /usr/local/info/ispell
#fi

#%preun
#if [ -x /usr/local/bin/install-info ] ; then
#	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
#		 /usr/local/info/ispell
#fi

%files
%defattr(-,bin,bin)
/usr/local/bin/ispell
/usr/local/bin/buildhash
/usr/local/bin/icombine
/usr/local/bin/ijoin
/usr/local/bin/munchlist
/usr/local/bin/findaffix
/usr/local/bin/tryaffix
/usr/local/bin/defmt-c
/usr/local/bin/defmt-sh
#/usr/local/bin/sq
#/usr/local/bin/unsq
/usr/local/man/man1/ispell.1
/usr/local/man/man1/sq.1
/usr/local/man/man1/buildhash.1
/usr/local/man/man1/munchlist.1
/usr/local/man/man1/findaffix.1
/usr/local/man/man1/tryaffix.1
/usr/local/man/man1/unsq.1
/usr/local/man/man5/ispell.5
/usr/local/man/man5/english.5
#/usr/local/info/ispell
/usr/local/lib/english.aff
/usr/local/lib/americanmed.hash
/usr/local/lib/american.hash
/usr/local/lib/english.hash
