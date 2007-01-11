Name:           rlwrap
Version:        0.28
Release:	1
Summary:        Readline wrapper
Group:          Applications/System
License:        GPL
URL:            http://utopia.knoware.nl/~hlub/rlwrap/
Source0:        http://utopia.knoware.nl/~hlub/rlwrap/%{name}-%{version}.tar.gz
BuildRequires:  readline5-devel
BuildRoot:      %{_tmppath}/%{name}--root

%description
rlwrap is a 'readline wrapper' that uses the GNU readline library to
allow the editing of keyboard input for any other command. Input
history is remembered across invocations, separately for each command;
history completion and search work as in bash and completion word
lists can be specified on the command line.

%prep
%setup -q

%build
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export LDFLAGS
./configure --prefix=/usr/local
make

%install
rm -rf %{buildroot}
make DESTDIR=${RPM_BUILD_ROOT} install

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc AUTHORS BUGS COPYING ChangeLog INSTALL NEWS README TODO
%attr(0755,root,root) 
/usr/local/bin/rlwrap
/usr/local/share/man/man1/rlwrap.1
%dir %{_datadir}/rlwrap
%{_datadir}/rlwrap/coqtop
%{_datadir}/rlwrap/ftp
%{_datadir}/rlwrap/testclient


%changelog
* Wed Jan 10 2007 Rob Zinkov <rzinkov@nbcs.rutgers.edu>
- Initial Build
