Name: calc
Version: 2.02f
Release: 2
Summary: Emacs Calc
Copyright: GPL
Group: Applications/Productivity
Source: calc-2.02f.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: emacs >= 20.7
BuildRequires: emacs >= 20.7

%description
Emacs Calc lets you turn Emacs into an Hewlett Packard calculator.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/emacs20/share/emacs/site-lisp/calc-2.02f
mkdir -p $RPM_BUILD_ROOT/usr/local/emacs20/info
cp Makefile *el *elc \
   $RPM_BUILD_ROOT/usr/local/emacs20/share/emacs/site-lisp/calc-2.02f
cp calc.info* $RPM_BUILD_ROOT/usr/local/emacs20/info

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF
To install calc, do this:

  cd /usr/local/emacs20/share/emacs/site-lisp/calc-2.02f
  touch ../../20.7/site-lisp/default.el
  make public

EOF
/usr/local/bin/install-info --info-dir=/usr/local/emacs20/info \
   --entry="* Calc: (calc).                                  Emacs calc." \
   /usr/local/emacs20/info/calc.info

%preun
cat <<EOF
To take calc off your system, remove the calc edits from your
default.el file.
EOF
/usr/local/bin/install-info --info-dir=/usr/local/emacs20/info \
   --delete /usr/local/emacs20/info/calc.info

%files
%defattr(-,bin,bin)
%doc calccard.tex calc.texinfo
/usr/local/emacs20/share/emacs/site-lisp/calc-2.02f
/usr/local/emacs20/info/*info*
