{-# LANGUAGE CPP #-}
{-# LANGUAGE NoRebindableSyntax #-}
{-# OPTIONS_GHC -fno-warn-missing-import-lists #-}
module Paths_haq (
    version,
    getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir,
    getDataFileName, getSysconfDir
  ) where

import qualified Control.Exception as Exception
import Data.Version (Version(..))
import System.Environment (getEnv)
import Prelude

#if defined(VERSION_base)

#if MIN_VERSION_base(4,0,0)
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#else
catchIO :: IO a -> (Exception.Exception -> IO a) -> IO a
#endif

#else
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#endif
catchIO = Exception.catch

version :: Version
version = Version [0,1,0,0] []
bindir, libdir, dynlibdir, datadir, libexecdir, sysconfdir :: FilePath

bindir     = "/Users/anterooikkonen/ohjelmointi/cookbook/haskell/haq/.cabal-sandbox/bin"
libdir     = "/Users/anterooikkonen/ohjelmointi/cookbook/haskell/haq/.cabal-sandbox/lib/x86_64-osx-ghc-8.4.3/haq-0.1.0.0-6OeqZIKhvEzIQegM9maown"
dynlibdir  = "/Users/anterooikkonen/ohjelmointi/cookbook/haskell/haq/.cabal-sandbox/lib/x86_64-osx-ghc-8.4.3"
datadir    = "/Users/anterooikkonen/ohjelmointi/cookbook/haskell/haq/.cabal-sandbox/share/x86_64-osx-ghc-8.4.3/haq-0.1.0.0"
libexecdir = "/Users/anterooikkonen/ohjelmointi/cookbook/haskell/haq/.cabal-sandbox/libexec/x86_64-osx-ghc-8.4.3/haq-0.1.0.0"
sysconfdir = "/Users/anterooikkonen/ohjelmointi/cookbook/haskell/haq/.cabal-sandbox/etc"

getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir, getSysconfDir :: IO FilePath
getBinDir = catchIO (getEnv "haq_bindir") (\_ -> return bindir)
getLibDir = catchIO (getEnv "haq_libdir") (\_ -> return libdir)
getDynLibDir = catchIO (getEnv "haq_dynlibdir") (\_ -> return dynlibdir)
getDataDir = catchIO (getEnv "haq_datadir") (\_ -> return datadir)
getLibexecDir = catchIO (getEnv "haq_libexecdir") (\_ -> return libexecdir)
getSysconfDir = catchIO (getEnv "haq_sysconfdir") (\_ -> return sysconfdir)

getDataFileName :: FilePath -> IO FilePath
getDataFileName name = do
  dir <- getDataDir
  return (dir ++ "/" ++ name)
