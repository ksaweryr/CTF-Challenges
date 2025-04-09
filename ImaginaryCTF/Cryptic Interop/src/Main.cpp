#include "org_imaginaryctf_CrypticInterop_Main.h"
#include "util.h"

JNIEXPORT jboolean JNICALL Java_org_imaginaryctf_CrypticInterop_Main_verify
  (JNIEnv * env, jobject obj, jstring jflag) {
    const char* flag = env->GetStringUTFChars(jflag, 0);
    int result = Verify(flag);
    env->ReleaseStringUTFChars(jflag, flag);

    return result;
}