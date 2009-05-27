Name:           suitesparse
Version:        3.2.0
Release:        1
Summary:        A collection of sparse matrix libraries

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://www.cise.ufl.edu/research/sparse/SuiteSparse
Source0:        http://www.cise.ufl.edu/research/sparse/SuiteSparse/SuiteSparse-%{version}.tar.gz
Patch0:		suitesparse_cstring.patch
Patch1:		suitesparse_config.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
suitesparse is a collection of libraries for computations involving sparse
matrices.  The package includes the following libraries:
  AMD         approximate minimum degree ordering
  BTF         permutation to block triangular form (beta)
  CAMD        constrained approximate minimum degree ordering
  COLAMD      column approximate minimum degree ordering
  CCOLAMD     constrained column approximate minimum degree ordering
  CHOLMOD     sparse Cholesky factorization
  CSparse     a concise sparse matrix package
  CXSparse    CSparse extended: complex matrix, int and long int support
  KLU         sparse LU factorization, primarily for circuit simulation
  LDL         a simple LDL' factorization
  SQPR        a multithread, multifrontal, rank-revealing sparse QR
              factorization method
  UMFPACK     sparse LU factorization
  UFconfig    configuration file for all the above packages.


%package devel
Summary:        Development headers for SuiteSparse
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
The suitesparse-devel package contains files needed for developing
applications which use the suitesparse libraries.


%package static
Summary:        Static version of SuiteSparse libraries
Group:          Development/Libraries
Requires:       %{name}-devel = %{version}-%{release}

%description static
The suitesparse-static package contains the statically linkable
version of the suitesparse libraries.



%prep
%setup -q -n SuiteSparse
%patch0 -p0
%patch1 -p1

%build
%define amd_version 2.2
%define amd_version_major 2
%define btf_version 1.0.1
%define btf_version_major 1
%define camd_version 2.2.0
%define camd_version_major 2
%define ccolamd_version 2.7.1
%define ccolamd_version_major 2
%define cholmod_version 1.7.0
%define cholmod_version_major 1
%define colamd_version 2.7.0
%define colamd_version_major 2
%define csparse_version 2.2.2
%define csparse_version_major 2
%define cxsparse_version 2.2.2
%define cxsparse_version_major 2
%define klu_version 1.0.1
%define klu_version_major 1
%define ldl_version 2.0.0
%define ldl_version_major 2
%define umfpack_version 5.2.0
%define umfpack_version_major 5
%define spqr_version 1.1.0
%define spqr_version_major 1
### CHOLMOD can also be compiled to use the METIS library.
### To compile with METIS, define enable_metis as 1 below.
%define enable_metis 0
### CXSparse is a superset of CSparse, and the two share common header
### names, so it does not make sense to build both. CXSparse is built
### by default, but CSparse can be built instead by defining
### enable_csparse as 1 below.
%define enable_csparse 0

PATH="/opt/SUNWspro/bin:${PATH}"
export PATH

mkdir Devel Devel/AMD Devel/CHOLMOD Devel/KLU Devel/LDL Devel/UMFPACK \
      Doc Doc/AMD Doc/BTF Doc/CAMD Doc/CCOLAMD Doc/CHOLMOD Doc/COLAMD \
      Doc/KLU Doc/LDL Doc/UMFPACK Doc/SPQR Lib Include

cd AMD/Lib
  gmake
cd ../../Lib
  cc -G -Wl,-soname,libamd.so.%{amd_version_major} -o \
     libamd.so.%{amd_version} ../AMD/Lib/*.o -lsunmath -lm
  ln -sf libamd.so.%{amd_version} libamd.so.%{amd_version_major}
  ln -sf libamd.so.%{amd_version} libamd.so
  cp -p ../AMD/Lib/*.a ./
cd ../AMD
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/License Doc/ChangeLog ../Doc/AMD
  cp -p Doc/*.pdf ../Devel/AMD
cd ..

cd BTF/Lib
  gmake
cd ../../Lib
  cc -G -Wl,-soname,libbtf.so.%{btf_version_major} -o \
     libbtf.so.%{btf_version} ../BTF/Lib/*.o
  ln -sf libbtf.so.%{btf_version} libbtf.so.%{btf_version_major}
  ln -sf libbtf.so.%{btf_version} libbtf.so
  cp -p ../BTF/Lib/*.a ./
cd ../BTF
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/* ../Doc/BTF
cd ..

cd CAMD/Lib
  gmake
cd ../../Lib
  cc -G -Wl,-soname,libcamd.so.%{camd_version_major} -o \
     libcamd.so.%{camd_version} ../CAMD/Lib/*.o -lsunmath -lm
  ln -sf libcamd.so.%{camd_version} libcamd.so.%{camd_version_major}
  ln -sf libcamd.so.%{camd_version} libcamd.so
  cp -p ../CAMD/Lib/*.a ./
cd ../CAMD
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/ChangeLog Doc/License ../Doc/CAMD
  cp -p Doc/*.pdf ../Devel/CAMD
cd ..

cd CCOLAMD/Lib
  gmake
cd ../../Lib
  cc -G -Wl,-soname,libccolamd.so.%{ccolamd_version_major} -o \
     libccolamd.so.%{ccolamd_version} ../CCOLAMD/Lib/*.o -lsunmath -lm
  ln -sf libccolamd.so.%{ccolamd_version} libccolamd.so.%{ccolamd_version_major}
  ln -sf libccolamd.so.%{ccolamd_version} libccolamd.so
  cp -p ../CCOLAMD/Lib/*.a ./
cd ../CCOLAMD
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/* ../Doc/CCOLAMD
cd ..

cd COLAMD/Lib
  gmake
cd ../../Lib
  cc -G -Wl,-soname,libcolamd.so.%{colamd_version_major} -o \
     libcolamd.so.%{colamd_version} ../COLAMD/Lib/*.o -lsunmath -lm
  ln -sf libcolamd.so.%{colamd_version} libcolamd.so.%{colamd_version_major}
  ln -sf libcolamd.so.%{colamd_version} libcolamd.so
  cp -p ../COLAMD/Lib/*.a ./
cd ../COLAMD
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/* ../Doc/COLAMD
cd ..

%if "%{?enable_metis}" == "1"
CHOLMOD_FLAGS="-I%{_includedir}/metis"
%else
CHOLMOD_FLAGS="-DNPARTITION"
%endif
cd CHOLMOD/Lib
  gmake CFLAGS="$CHOLMOD_FLAGS"
cd ../../Lib
  cc -G -Wl,-soname,libcholmod.so.%{cholmod_version_major} -o \
     libcholmod.so.%{cholmod_version} ../CHOLMOD/Lib/*.o \
     -xlic_lib=sunperf libamd.so.%{amd_version_major} \
     libcamd.so.%{camd_version_major} libcolamd.so.%{colamd_version_major} \
     libccolamd.so.%{ccolamd_version_major} -lsunmath -lm
  ln -sf libcholmod.so.%{cholmod_version} libcholmod.so.%{cholmod_version_major}
  ln -sf libcholmod.so.%{cholmod_version} libcholmod.so
  cp -p ../CHOLMOD/Lib/*.a ./
cd ../CHOLMOD
  cp -p Include/*.h ../Include
  cp -p README.txt ../Doc/CHOLMOD
  cp -p Cholesky/License.txt ../Doc/CHOLMOD/Cholesky_License.txt
  cp -p Core/License.txt ../Doc/CHOLMOD/Core_License.txt
  cp -p MatrixOps/License.txt ../Doc/CHOLMOD/MatrixOps_License.txt
  cp -p Partition/License.txt ../Doc/CHOLMOD/Partition_License.txt
  cp -p Supernodal/License.txt ../Doc/CHOLMOD/Supernodal_License.txt
  cp -p Doc/*.pdf ../Devel/CHOLMOD
cd ..

%if "%{?enable_csparse}" == "1"
cd CSparse/Source
  gmake    
  cp -p cs.h ../../Include
cd ../../Lib
  cc -G -Wl,-soname,libcsparse.so.%{csparse_version_major} -o \
     libcsparse.so.%{csparse_version} ../CSparse/Source/*.o -lsunmath -lm
  ln -sf libcsparse.so.%{csparse_version} libcsparse.so.%{csparse_version_major}
  ln -sf libcsparse.so.%{csparse_version} libcsparse.so
  cp -p ../CSparse/Source/*.a ./
cd ../CSparse
  mkdir ../Doc/CSparse/
  cp -p Doc/* ../Doc/CSparse
cd ..

%else
cd CXSparse/Lib
  gmake
cd ../../Lib
  cc -G -Wl,-soname,libcxsparse.so.%{cxsparse_version_major} -o \
     libcxsparse.so.%{cxsparse_version} ../CXSparse/Lib/*.o -lsunmath -lm
  ln -sf libcxsparse.so.%{cxsparse_version} libcxsparse.so.%{cxsparse_version_major}
  ln -sf libcxsparse.so.%{cxsparse_version} libcxsparse.so
  cp -p ../CXSparse/Lib/*.a ./
cd ../CXSparse
  cp -p Include/cs.h ../Include
  mkdir ../Doc/CXSparse/
  cp -p Doc/* ../Doc/CXSparse
cd ..
%endif

cd KLU/Lib
  gmake  
cd ../../Lib
  cc -G -Wl,-soname,libklu.so.%{klu_version_major} -o \
     libklu.so.%{klu_version} ../KLU/Lib/*.o \
     libamd.so.%{amd_version_major} libcolamd.so.%{colamd_version_major} \
     libbtf.so.%{btf_version_major} libcholmod.so.%{cholmod_version_major}
  ln -sf libklu.so.%{klu_version} libklu.so.%{klu_version_major}
  ln -sf libklu.so.%{klu_version} libklu.so
  cp -p ../KLU/Lib/*.a ./
cd ../KLU
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/lesser.txt ../Doc/KLU
cd ..

cd LDL/Lib
    gmake
cd ../../Lib
  cc -G -Wl,-soname,libldl.so.%{ldl_version_major} -o \
     libldl.so.%{ldl_version} ../LDL/Lib/*.o
  ln -sf libldl.so.%{ldl_version} libldl.so.%{ldl_version_major}
  ln -sf libldl.so.%{ldl_version} libldl.so
  cp -p ../LDL/Lib/*.a ./
cd ../LDL
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/ChangeLog Doc/lesser.txt ../Doc/LDL
  cp -p Doc/*.pdf ../Devel/LDL
cd ..

cd UMFPACK/Lib
  gmake
cd ../../Lib
  cc -G -Wl,-soname,libumfpack.so.%{umfpack_version_major} -o \
     libumfpack.so.%{umfpack_version} ../UMFPACK/Lib/*.o \
     -xlic_lib=sunperf libamd.so.%{amd_version_major} -lsunmath -lm
  ln -sf libumfpack.so.%{umfpack_version} libumfpack.so.%{umfpack_version_major}
  ln -sf libumfpack.so.%{umfpack_version} libumfpack.so
  cp -p ../UMFPACK/Lib/*.a ./
cd ../UMFPACK
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/License Doc/ChangeLog Doc/gpl.txt ../Doc/UMFPACK
  cp -p Doc/*.pdf ../Devel/UMFPACK
cd ..

cd SPQR/Lib
  gmake CFLAGS="-DNPARTITION"
cd ../../Lib
  CC -G -Wl,-soname,libspqr.so.%{spqr_version_major} -o \
     libspqr.so.%{spqr_version} ../SPQR/Lib/*.o \
     -xlic_lib=sunperf \
     libcholmod.so.%{cholmod_version_major} -lsunmath -lm
  ln -sf libspqr.so.%{spqr_version} libspqr.so.%{spqr_version_major}
  ln -sf libspqr.so.%{spqr_version} libspqr.so
  cp -p ../SPQR/Lib/*.a ./
cd ../SPQR
  cp -p Include/*.h* ../Include
  cp -p README{,_SPQR}.txt
  cp -p README_SPQR.txt Doc/* ../Doc/SPQR
cd ..

cp -p UFconfig/UFconfig.h Include

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}
mkdir -p ${RPM_BUILD_ROOT}%{_includedir}/%{name}
cd Lib
  for f in *.a *.so*; do
    cp -a $f ${RPM_BUILD_ROOT}%{_libdir}/$f
  done
cd ..
cd Include
  for f in *.h;  do
    cp -a $f ${RPM_BUILD_ROOT}%{_includedir}/%{name}/$f
  done
cd ..


%clean
rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-,root,root)
%doc Doc/*
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%doc Devel/*
%{_includedir}/%{name}
%{_libdir}/lib*.so

%files static
%defattr(-,root,root)
%{_libdir}/lib*.a

%changelog

