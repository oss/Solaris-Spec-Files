Name: cweb
Version: 3.6
Release: 2
Summary: Literate programming in C
Copyright: Freely distributable
Group: Development/Tools
Source: cweb.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: teTeX
BuildRequires: teTeX
BuildRequires: emacs

%description
Literate programming is a method of programming where documentation
and code are written concurrently in the same source file.  Cweb is a
literate version of the C progamming language (it also has support for
C++).  Install this package if you want to compile or write literate
programs.

%prep
%setup -T -c cweb-%{version}
%setup -q -D -T -a 0 -n cweb-%{version}
find . -exec touch \{\} \;

%build
make CC=gcc
make doc
make usermanual
make fullmanual

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/local/teTeX/share/texmf/tex/cweb
mkdir -p $RPM_BUILD_ROOT/usr/local/lib/cweb
mkdir -p $RPM_BUILD_ROOT/usr/local/emacs20/share/emacs/site-lisp
/bin/cp cweave $RPM_BUILD_ROOT/usr/local/bin/cweave
chmod 755 $RPM_BUILD_ROOT/usr/local/bin/cweave
/bin/cp ctangle $RPM_BUILD_ROOT/usr/local/bin/ctangle
chmod 755 $RPM_BUILD_ROOT/usr/local/bin/ctangle
/bin/cp cweb.1 $RPM_BUILD_ROOT/usr/local/man/man1/cweb.1
chmod 644 $RPM_BUILD_ROOT/usr/local/man/man1/cweb.1
/bin/cp cwebmac.tex $RPM_BUILD_ROOT/usr/local/teTeX/share/texmf/tex/cweb
chmod 644 $RPM_BUILD_ROOT/usr/local/teTeX/share/texmf/tex/cweb/cwebmac.tex
/bin/cp cweb.el $RPM_BUILD_ROOT/usr/local/emacs20/share/emacs/site-lisp
chmod 644 $RPM_BUILD_ROOT/usr/local/emacs20/share/emacs/site-lisp/cweb.el
/bin/cp c++lib.w $RPM_BUILD_ROOT/usr/local/lib/cweb
chmod 644 $RPM_BUILD_ROOT/usr/local/lib/cweb/c++lib.w

%post
echo "You need to run mktexlsr."

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc examples common.dvi ctangle.dvi cweave.dvi cwebman.dvi
/usr/local/bin/cweave
/usr/local/bin/ctangle
/usr/local/man/man1/cweb.1
/usr/local/teTeX/share/texmf/tex/cweb
/usr/local/emacs20/share/emacs/site-lisp/cweb.el
/usr/local/lib/cweb
