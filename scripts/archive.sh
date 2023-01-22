#!/bin/bash

cat <<EOF
---
title: آرشیو
---

# آرشیو آزمون‌های المپیاد کامپیوتر

## مرحله اول و دوم

!!! info "نکته"

    جدول زیر به مرور زمان آپدیت می‌شود.

<style>
    .md-typeset__table {
        display: block !important;
    }
    table {
        display: table !important;
    }
</style>

$(python -m scripts generate-table -f $1)

- [کتاب پاسخی بر المپیاد‌های کامپیوتر ایران، نوشته آقای یاسر احمدی فولادی](https://shaazzz.s3.ir-thr-at1.arvanstorage.com/src/other/fuladi.pdf)
سوالات و پاسخنامه‌های مرحله دوم دوره‌های ۱ تا ۱۳ رو شامل میشه. پی‌دی‌اف کتاب به دلیل چاپ نشدن مجدد کتاب و با اجازه نویسنده در دسترس عموم قرار گرفته.

## آزمون‌های شاززز

همه‌ی آزمون‌های شاززز رو می‌تونید از
[این لینک](https://github.com/shaazzz/shaazzz-exam)
ببینید و دانلود کنید.
EOF