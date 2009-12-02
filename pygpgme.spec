%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           pygpgme
Version:        0.1
Release:        18.20090824bzr68%{?dist}
Summary:        Python module for working with OpenPGP messages

Group:          Development/Languages
License:        LGPLv2+
URL:            http://cheeseshop.python.org/pypi/pygpgme/0.1
# pygpgme is being developed for Ubuntu and built for Ubuntu out of
# launchpad's source control.  So we need to create snapshots.
# At this time, updated packages from launchpad have fixed tests and support
# for generating keys
#
# Steps to create snapshot:
# bzr branch lp:pygpgme -r68
# cd pygpgme
# patch -p0 < ../pygpgme-examples.patch
# python setup.py sdist
# tarball is in dist/pygpgme-0.1.tar.gz
Source0:        pygpgme-0.1.tar.gz
#Source0:        http://cheeseshop.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
# Patch to make generating a tarball (sdist) work.  Applied prior to creating
# the Source0.
Patch100:       pygpgme-examples.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  python
BuildRequires:  gpgme-devel

%description
PyGPGME is a Python module that lets you sign, verify, encrypt and decrypt
files using the OpenPGP format.  It is built on top of GNU Privacy Guard and
the GPGME library.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:/usr/ccs/bin:${PATH}"
CC="cc" CXX="CC" CFLAGS="-I/usr/local/include -O2 -g" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CFLAGS LD LDFLAGS
%{__python} setup.py build_ext -I/usr/local/include -L/usr/local/lib -R/usr/local/lib
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT
chmod 0755 $RPM_BUILD_ROOT%{python_sitearch}/gpgme/_gpgme.so

%clean
rm -rf $RPM_BUILD_ROOT

### Can't enable the tests because they depend on importing a private key.
# gpg2 on which our gpgme library depends does not import private keys so this
# won't work.  The issue in the real world is not so big as we  don't
# manipulate private keys outside of a keyring that often.
#%check
# Use the installed gpgme because it has the built compiled module
#mv gpgme gpgme.bak
#ln -s $RPM_BUILD_ROOT%{python_sitearch}/gpgme .
#python test_all.py

%files
%defattr(-,root,root,-)
%doc README PKG-INFO
%{python_sitearch}/*
# No need to ship the tests
%exclude %{python_sitearch}/gpgme/tests/


%changelog
* Wed Dec 02 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.1-18.20090824bzr68
- I will not publish unsigned packages again

* Wed Nov 04 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.1-17.20090824bzr68
- Solaris port

* Mon Aug 24 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 0.1-16.20090824bzr68
- Rebase to new upstream snapshot
- Patches merged upstream
- Fixes deprecation warnings on py2.6/py3.0
- Remove py2.3 patch -- only needed for EPEL-4

* Tue Jul 28 2009 Jesse Keating <jkeating@redhat.com> - 0.1-15.20090121bzr54
- Add a second patch from mitr for symmetric_encryption_support

* Tue Jul 28 2009 Jesse Keating <jkeating@redhat.com> - 0.1-14.20090121bzr54
- Patch from mitr for gpgme_ctx_set_engine_info

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-13.20090121bzr54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-12.20090121bzr54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 22 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 0.1-11.20090121bzr54
- Add patch to cvs.

* Wed Jan 21 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 0.1-10.20090121bzr54
- Update to upstream snapshot.

* Fri Nov 28 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.1-9
- Rebuild for Python 2.6

* Fri Feb 8 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 0.1-8
- Rebuild for new gcc.

* Thu Jan 3 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 0.1-7
- Include egg-info files.

* Fri May 18 2007 Toshio Kuratomi <toshio@tiki-lounge.com> - 0.1-6
- Rebuild to pick up enhancements from gcc on F-8.
- Update licensing to conform to new guidelines.

* Fri May 18 2007 Toshio Kuratomi <toshio@tiki-lounge.com> - 0.1-5
- Rebuild because of a bug in linking to an early version of the python-2.5
  package,

* Mon Oct 23 2006 Toshio Kuratomi <toshio@tiki-lounge.com> - 0.1-4
- Bump and rebuild for python 2.5 on devel.

* Mon Oct 23 2006 Toshio Kuratomi <toshio@tiki-lounge.com> - 0.1-3
- Add a patch to work under Python 2.3.
- Stop shipping the tests as they are useless to the end user.

* Fri Oct 13 2006 Toshio Kuratomi <toshio@tiki-lounge.com> - 0.1-2
- Change URL to cheeseshop

* Sun Oct 08 2006 Toshio Kuratomi <toshio@tiki-lounge.com> - 0.1-1
- Initial build for Fedora Extras. 
