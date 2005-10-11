#%include perl-header.spec
# Don't include the perl-header, all macros needed are below.
# Some macros defined in the header prevent easy upgrade to new version of
# perl without breaking current stable versions.
#
# Also, remote_rpm is stupid in respect to macro parsing (it just blazes
# through the file looking for defines once and doesn't do any test,
# which is a PITA when you are dealing with muti-arch mumbo-jumbo).
#
# Just a reminder, when OSS stablizes on a new version, be sure to update
# the perl-header file.
#

%define perl_version	  5.8.7
%define perl_release      1
%define perl_prefix	  /usr/local/perl5
%define perl_arch	  sun4-solaris-thread-multi
%define global_perl	  %{perl_prefix}/lib/%{perl_version}
%define global_perl_arch  %{global_perl}/%{perl_arch}
%define site_perl	  %{perl_prefix}/lib/site_perl/%{perl_version}
%define site_perl_arch	  %{site_perl}/%{perl_arch}
%define perl_binary	  %{perl_prefix}/bin/perl


Name: perl
Version: %{perl_version}
Release: %{perl_release}
Copyright: GPL/Artistic License
Group: Development/Languages
Provides: perl
Source: perl-%{version}.tar.gz
Summary: the Practical Extraction and Report Language
BuildRoot: /var/tmp/%{name}-root
BuildRequires: gdbm db 

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
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:/usr/openwin/bin:/usr/local/bin:/usr/local/gnu/bin:/usr/bin:/usr/sbin:/bin:/sbin"
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
%defattr(-,root,bin)
EOF
cat <<EOF > REGULAR-LIST
%defattr(-,root,bin)
%doc Copying Artistic README
EOF

find $RPM_BUILD_ROOT ! -type d \( -name \*.h -o -name \*.a \) -print \
    | sed "s#^$RPM_BUILD_ROOT/*#/#" >> DEVEL-LIST
find $RPM_BUILD_ROOT%{perl_prefix} -type d \
    | sed "s#^$RPM_BUILD_ROOT/*#%dir /#" >> REGULAR-LIST
find $RPM_BUILD_ROOT ! -type d ! \( -name \*.h -o -name \*.a \) -print \
    | sed "s#^$RPM_BUILD_ROOT/*#/#" >> REGULAR-LIST

# There is a dependancy on python for the unhardlinkify script,
# not sure if that should be be listed in the BuildReq, so it isn't.
# (It's should be in the build machines anyway)
cd $RPM_BUILD_ROOT
python /usr/local/bin/unhardlinkify.py ./

%clean
rm -rf $RPM_BUILD_ROOT

%files -f REGULAR-LIST

%files devel -f DEVEL-LIST
