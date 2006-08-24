Summary: xterm with 256 color suppport and uxterm: a unicode xterm
Name: xterm256
Version: 215
Release: 1
License: XFree86
Group: Applications/Terminals
Source: xterm.tar.gz
Packager: John M. Santel <jmsl@nbcs.rutgers.edu>
BuildRoot: /var/tmp/xterm-%{version}-root
BuildRequires: freetype2-devel

%description
xterm is the original terminal emulator for X. This version is included
in XFree86 and should be less buggy and more configurable than the one
included by Sun in Solaris. 

A version of xterm with unicode support is also included called uxterm.

%prep
%setup -n xterm-%{version}

%build
CC=/opt/SUNWspro/bin/cc
PATH=/opt/SUNWspro/bin:/usr/ccs/bin:/usr/local/gnu/bin:/usr/openwin/bin:/usr/local/bin:$PATH

export PATH CC

./configure --enable-256-color  --with-terminal-type=xterm-256
make 


%install
mkdir -p %{buildroot}/usr/local/share/doc/xterm
cp README.i18n %{buildroot}/usr/local/share/doc/xterm
make install DESTDIR=%{buildroot}
TERMINFO=`pwd`
export TERMINFO
tic terminfo
mkdir -p %{buildroot}/usr/share/lib/terminfo/x
rm x/xterm
rm x/xterms
cp x/* %{buildroot}/usr/share/lib/terminfo/x


%post
cat << EOF
To use this version of xterm (and not the default Solaris version) make sure /usr/local/bin
occurs before /usr/openwin/bin in your path. 

In order not to clobber the default xterm terminfo, this build of xterm 
indentifies itself as xterm-256, since it has support for 256 colors. This may 
be an issue if you are ssh-ing to a computer where this version is not 
installed. You may have to set the terminal type manually in your .bashrc or 
.cshrc. To ensure that a foreign machine completely supports 
all of the escapes for this version of xterm you may also want to run 
infocmp xterm-256color > .xterm-256 
and scp it to the remote machine and add something like this to the .bashrc of 
the remote machine.

.bashrc

if [ "$TERM" == "xterm-256" ]; then
        export TERMINFO=/your/home/directory/.xterm-256
        export TERM=xterm
fi

This version also installed uxterm, which is a unicode version of xterm.

EOF
%clean
rm -rf {buildroot}

%files
%defattr(-, root, root)
/usr/local/bin/xterm
/usr/local/bin/uxterm
/usr/local/bin/resize
/usr/local/man/man1/*
/usr/local/share/doc/xterm/*
/usr/local/lib/X11/app-defaults/XTerm
/usr/local/lib/X11/app-defaults/XTerm-color
/usr/local/lib/X11/app-defaults/UXTerm
/usr/share/lib/terminfo/x
