Summary: Plan 9-style terminal
Name: 9term
Version: 1.6.3
Release: 2
Group: User Interface/X
License: Freely distributable
Source: 9term-working.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: 9libs
BuildRequires: 9libs-devel

%description
This package contains a plan 9-style terminal.

%prep
%setup -q -n 9term

# 9term-working differs from the "real" 9term sources in two ways: the
# killpg function has been renamed so as not to collide with libc
# killpg; and the Makefile was rewritten so it would work.

%build
cd libtext
make
cd ../9term
make

%install
rm -rf $RPM_BUILD_ROOT

for i in include lib bin man/man1 man/man3; do
    mkdir -p $RPM_BUILD_ROOT/usr/local/$i
done

install -m 0644 libtext/text.h $RPM_BUILD_ROOT/usr/local/include/text.h
install -m 0644 libtext/libtext.a $RPM_BUILD_ROOT/usr/local/lib/libtext.a
install -m 0644 libtext/scroll.3 $RPM_BUILD_ROOT/usr/local/man/man3/scroll.3
install -m 0644 libtext/text.3 $RPM_BUILD_ROOT/usr/local/man/man3/text.3
install -m 0755 9term/9term $RPM_BUILD_ROOT/usr/local/bin/9term
install -m 0755 9term/wloc $RPM_BUILD_ROOT/usr/local/bin/wloc
install -m 0644 9term/9term.1 $RPM_BUILD_ROOT/usr/local/man/man1/9term.1

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF

To complete this installation, you need to add a terminfo entry.  Run
sh in 9term.  As root, run
   
  echo \$TERMCAP | captoinfo > 9term.ti
  tic 9term.ti
  
EOF

%files
%defattr(-,bin,bin)
/usr/local/include/*
/usr/local/lib/*
/usr/local/bin/*

