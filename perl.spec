%include perl-header.spec

Name: perl
Version: %{perl_version}
Release: 5
Copyright: GPL/Artistic License
Group: Development/Languages
Provides: perl
Source: stable561.tar.gz
Summary: the Practical Extraction and Report Language
BuildRoot: /var/tmp/%{name}-root
BuildRequires: gdbm db 
# Not really:
# Conflicts: vpkg-SUNWpl5u vpkg-SUNWpl5p vpkg-SUNWpl5m

%description
Perl is an extremely powerful scripting language that is widely used
both as an administration tool and as one of the languages of choice
for CGI scripts.  Install this if you want to use perl.

%package devel
Summary: Header files and static libraries for Perl
Group: Development/Languages
Requires: perl = %{version}

%description devel
Perl-devel contains the Perl header files and static libraries

%prep
%setup -q

%build
PATH="/usr/openwin/bin:/opt/SUNWspro/bin:/usr/local/bin:/usr/local/gnu/bin:/usr/ccs/bin:/usr/bin:/usr/sbin"
export PATH

# really should be Sun's CC
#sh Configure -de -Dprefix=%{perl_prefix} -Dcpp='/usr/local/bin/gcc -E' \
#             -Dinstallprefix="$RPM_BUILD_ROOT%{perl_prefix}" \
#             -Dcc='/usr/local/bin/gcc' \
#             -Dldflags='-L/usr/local/lib -R/usr/local/lib' -Dusethreads
sh Configure -de -Dprefix=%{perl_prefix} -Dusethreads \
	-Dldflags='-L/usr/local/lib -R/usr/local/lib' \
	-Dinstallprefix="$RPM_BUILD_ROOT%{perl_prefix}"
make
make test

%install
build_dir=`pwd`
rm -rf $RPM_BUILD_ROOT
for d in bin usr/bin usr/local/bin ; do
    mkdir -p $RPM_BUILD_ROOT/$d
done
make install

# clean up files which know about the build root
for fn in .packlist Config.pm ; do
    afn="$RPM_BUILD_ROOT%{global_perl_arch}/$fn"
    chmod 0644 $afn
    mv $afn $afn.TEMP
    sed "s#$RPM_BUILD_ROOT##g" < $afn.TEMP > $afn
    rm -f $afn.TEMP
done
chmod 0444 \
  $RPM_BUILD_ROOT%{global_perl_arch}/Config.pm

cat <<EOF > DEVEL-LIST
%defattr(-,root,root)
EOF
cat <<EOF > REGULAR-LIST
%defattr(-,root,root)
%doc Copying Artistic README
EOF

find $RPM_BUILD_ROOT ! -type d \( -name \*.h -o -name \*.a \) -print \
    | sed "s#^$RPM_BUILD_ROOT/*#/#" >> DEVEL-LIST
find $RPM_BUILD_ROOT%{perl_prefix} -type d \
    | sed "s#^$RPM_BUILD_ROOT/*#%dir /#" >> REGULAR-LIST
find $RPM_BUILD_ROOT ! -type d ! \( -name \*.h -o -name \*.a \) -print \
    | sed "s#^$RPM_BUILD_ROOT/*#/#" >> REGULAR-LIST

%clean
rm -rf $RPM_BUILD_ROOT

%files -f REGULAR-LIST

%files devel -f DEVEL-LIST
