%global  kf_version 6.18.0

Name:    kf6-solid
Summary: Desktop hardware abstraction
Version: 6.18.0
Release: 1%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/solid
Source0: %{name}-%{version}.tar.bz2

# upstream patches

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: flex
BuildRequires: bison

BuildRequires: pkgconfig(mount)
BuildRequires: pkgconfig(udev)



BuildRequires: kf6-rpm-macros
BuildRequires: kf6-extra-cmake-modules >= %{kf_version}

BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qttools-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kcoreaddons-devel
#BuildRequires: kf6-ki18n-devel

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake_kf6 \
  -DUSE_DBUS=ON \
  -DUDEV_DISABLED=OFF \
  %{nil}

%cmake_build

%install
%cmake_install

%find_lang_kf6 solid6_qt

%files -f solid6_qt.lang
%license LICENSES/*
%{_kf6_bindir}/solid-hardware6
%{_kf6_libdir}/libKF6Solid.so.*
%{_kf6_datadir}/qlogging-categories6/*.categories
%{_kf6_datadir}/qlogging-categories6/*.renamecategories

%files devel
%{_kf6_includedir}/Solid
%{_kf6_libdir}/cmake/KF6Solid
%{_kf6_libdir}/libKF6Solid.so
