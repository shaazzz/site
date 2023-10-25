#!/bin/bash

cat <<EOF
---
title: آرشیو
---

# آرشیو آزمون‌های المپیاد کامپیوتر

## سوالات و پاسخنامه‌های رسمی مرحله اول، دوم و سوم

<style>
    .md-typeset__table {
        display: block !important;
    }
    table {
        display: table !important;
    }
</style>

$(python -m scripts generate-table -f $1)

- [کتاب پاسخی بر المپیاد‌های کامپیوتر ایران، نوشته آقای یاسر احمدی فولادی](https://shaazzz.s3.ir-thr-at1.arvanstorage.ir/src/other/fuladi.pdf)
سوالات و پاسخنامه‌های مرحله دوم دوره‌های ۱ تا ۱۳ رو شامل میشه. پی‌دی‌اف کتاب به دلیل چاپ نشدن مجدد کتاب و با اجازه نویسنده در دسترس عموم قرار گرفته.

- پاسخ عددی سوالات مرحله سوم داخل
[اپدیا](https://opedia.ir/%D8%B3%D9%88%D8%A7%D9%84%D8%A7%D8%AA_%D8%A7%D9%84%D9%85%D9%BE%DB%8C%D8%A7%D8%AF/%D9%85%D8%B1%D8%AD%D9%84%D9%87_%DB%8C_%D8%B3%D9%88%D9%85/%D9%81%D9%87%D8%B1%D8%B3%D8%AA)
قرار داره و راه‌حل‌هاشون از
[گیت‌هاب](https://github.com/shaazzz/M3-Archive/)
قابل دسترسه.

## آزمون‌های شاززز

همه‌ی آزمون‌های شاززز رو می‌تونید از
[این لینک](https://github.com/shaazzz/shaazzz-exam)
ببینید و دانلود کنید.
EOF
