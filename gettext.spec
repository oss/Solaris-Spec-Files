Name: gettext
Version: 0.11.5
Copyright: GPL
Group: Development/Tools
Summary: Internationalization tools
Release: 1ru
Source: gettext-0.11.5.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: emacs

%description
GNU gettext is a tool that helps programmers write programs that
are "portable" culturally: by marking strings in your program that
potentially should be in several languages and compiling with gettext,
you can add translations with minimum effort.  Install gettext if you
are developing software that potentially would be used by non-English
speakers or compiling software that requires it.

%prep
%setup -q
rm doc/gettext.info

%build
./configure --prefix=/usr/local
make
cd doc
make info gettext.texi

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/info/gettext.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/gettext.info
fi

%files
%defattr(-,root,root)
%doc COPYING
/usr/local/info/*.info*
/usr/local/share/gettext/intl/*
/usr/local/share/gettext/po/Makefile.in.in
/usr/local/share/gettext/ABOUT-NLS
/usr/local/share/aclocal/*
#/usr/local/share/emacs/site-lisp/*
/usr/local/share/locale/locale.alias
/usr/local/bin/*
/usr/local/share/locale/*/LC_MESSAGES/gettext.mo
