Name: groff
Version: 1.17.2
Copyright: GPL
Group: Applications/Publishing
Summary: GNU troff
Release: 1
Source: groff-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
GNU troff is a typesetting system.  Groff, like TeX, is not a
WYSIWYG system.  Instead, you write text files that include special
typesetting commands and then run them through groff.  Groff includes
special preprocessors for typesetting equations, pictures, and tables.
You should install this package if you need the GNU extensions to troff.

%prep
%setup -q

%build
./configure --prefix=/usr/local/gnu
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/gnu/info
make install prefix=%{buildroot}/usr/local/gnu
cd doc 
# inexplicably, makeinfo fails on solaris 6
set +e; makeinfo groff.texinfo || touch %{buildroot}/usr/local/gnu/info/groff.BAD
cp -pr groff groff-? %{buildroot}/usr/local/gnu/info
touch %{buildroot}/usr/local/gnu/info/groff

%clean
rm -rf %{buildroot}

%post
if [ -x /usr/local/bin/install-info -a \! -r /usr/local/info/groff.BAD ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/gnu/info \
		 /usr/local/gnu/info/groff
fi

%preun
if [ -x /usr/local/bin/install-info -a \! -r /usr/local/info/groff.BAD ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/gnu/info \
		 /usr/local/gnu/info/groff
fi

%files
%defattr(-,root,root)
%doc COPYING doc/*me doc/*ms doc/*g doc/groff.texinfo
/usr/local/gnu/man/*/*
/usr/local/gnu/bin/*
/usr/local/gnu/share/groff
/usr/local/gnu/lib/groff
/usr/local/gnu/info/groff*
