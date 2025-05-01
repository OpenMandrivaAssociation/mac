%define _version 1109

Name:		mac
Version:	11.09
Release:	1
Summary:	APE codec and decompressor
License:	BSD-3-Clause
Group:		Sound/Utilities
URL:		https://www.monkeysaudio.com/index.html
Source0:	https://monkeysaudio.com/files/MAC_%{_version}_SDK.zip
BuildSystem:	cmake

BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	unzip

%description
Monkey’s Audio is a fast and easy way to compress digital music.
Unlike traditional methods such as mp3, ogg, or wma that permanently
discard quality to save space, Monkey’s Audio only makes perfect,
bit-for-bit copies of your music.

%package devel
Summary:	Development files for APE
Requires:	mac = %{version}-%{release}

%description devel
Development files for Monkey's Audio Codec and decompressor.

%prep
%setup -qc
tr -d '\r' <Readme.txt >README

%build
cmake \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DCMAKE_C_FLAGS="%{optflags}" \
    -DCMAKE_CXX_FLAGS="%{optflags}" \
	-DBUILD_SHARED=ON \
	-DBUILD_UTIL=ON \
	-G Ninja
%ninja_build

%install
%ninja_install


%files
%{_bindir}/%{name}
%{_libdir}/libMAC.so.*
%doc README
%license License.txt

%files devel
%{_includedir}/MAC
%{_libdir}/libMAC.so
