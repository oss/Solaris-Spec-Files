Name: a2ps
Version: 4.12
Release: 4
Copyright: GPL
Group: Applications/Printing
Summary: ASCII to PS
Source: a2ps-4.12.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: gs-fonts psutils

%description
   a2ps formats files for printing on a PostScript printer.

   The format used is nice and compact: normally two pages on each
physical page, borders surrounding pages, headers with useful
information (page number, printing date, file name or supplied header),
line numbering, pretty-printing, symbol substitution etc.  This is very
useful for making archive listings of programs or just to check your
code in the bus.  Actually a2ps is kind of boostrapped: its sources are
frequently printed with a2ps `:)'.

   While at the origin its names was derived from "ASCII to PostScript",
today we like to think of it as "Any to PostScript".  Indeed, a2ps
supports "delegations", i.e., you can safely use a2ps to print DVI,
PostScript, LaTeX, JPEG etc., even compressed.

       [from the Info documentation]

%prep
%setup -q

%build
./configure --prefix=/usr/local --enable-shared
make LDFLAGS="-R/usr/local/lib"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/info/ogonkify.info
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/info/a2ps.info
	/usr/local/bin/install-info --info-dir=/usr/local/info \
		 /usr/local/info/regex.info
fi

%preun
if [ -x /usr/local/bin/install-info ] ; then
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/ogonkify.info
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/a2ps.info
	/usr/local/bin/install-info --delete --info-dir=/usr/local/info \
		 /usr/local/info/regex.info
fi

%files
%defattr(-,bin,bin)
/usr/local/share/a2ps
/usr/local/share/ogonkify
/usr/local/share/emacs/site-lisp/*.el
/usr/local/etc/*
/usr/local/info/*.info*
/usr/local/man/man1/*
/usr/local/bin/*
/usr/local/lib/lib*.so*
/usr/local/lib/lib*a
/usr/local/lib/locale/*/LC_MESSAGES/a2ps.mo
/usr/local/include/liba2ps.h
