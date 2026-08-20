---
generator: db-snooper
version: 0.0.31
generated_at_utc: 2026-08-20T17:29:07.408953Z
dialect: sqlite
database: /var/folders/9j/b9bx_drd53sc6zbpsqyrjy4h0000gn/T/dbsnoop-xqd5sny4/log.sqlite
schema: main
---

# "access_log"  (rows=30)

columns:
"session" varchar255: 22 distinct
"user_id" varchar255: "U001"=7, "U002"=4, "0CVKaz"=2, "1QceiB"=2, "1hI43A"=2, "2mmGwD"=2, "3cv4gm"=2, "AAuoEU"=2, "2bGs3i"=1, "2is8PX"=1, "3CEHe1"=1, "3Gv8vO"=1, "690mvB"=1, "6oABhM"=1, "7jjxQX"=1
"action" varchar255: "view"=11, "1CwlSX"=4, "6SN6DD"=4, "3JMO2k"=3, "EFnoNR"=2, "FGkTe9"=2, "KBlKgT"=2, "7Dn99b"=1, "KKTw9P"=1
"stamp" varchar255: "/detail"=7, "/search"=6, "/top"=6, "2016-01-01 18:00:00"=1, "2016-01-02 20:00:00"=1, "2016-01-03 22:00:00"=1, "2016-01-04 23:00:00"=1, "2016-01-05 00:30:00"=1, "2016-01-06 02:30:00"=1, "2016-01-07 03:30:00"=1, "2016-01-08 04:00:00"=1, "2016-01-09 12:00:00"=1, "2016-01-10 13:00:00"=1, "2016-01-11 15:00:00"=1

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| session | eee2b2 | 1cf768 | 2016-10-01 17:00:00 |
| user_id | U002 | U002 | 2bGs3i |
| action | view | view | 1CwlSX |
| stamp | 2016-01-10 13:00:00 | 2016-01-04 23:00:00 | /top |

# "action_log"  (rows=120)

columns:
"session" varchar255: "989004ea"=72, "47db0370"=18, "87b5725f"=18, "9afaf87c"=12
"user_id" varchar255: "U001"=91, "U002"=29
"action" varchar255: "add_cart"=72, "purchase"=30, "favorite"=6, "review"=6, "view"=6
"category" varchar255: "drama"=90, "action"=24, nulls=6
"products" varchar255: "D001"=54, "D001,D002"=18, "D002"=18, "A004"=6, "A005"=6, "A005,A006"=6, "A006"=6, nulls=6
"amount" int: 1000=18, 2000=12, nulls=90
"stamp" varchar255: "2016-11-03 18:00:00"=48, "2016-11-04 12:00:00"=18, "2016-11-03 18:10:00"=12, "2016-11-03 18:01:00"=6, "2016-11-03 18:02:00"=6, "2016-11-03 19:00:00"=6, "2016-11-03 20:00:00"=6, "2016-11-03 20:30:00"=6, "2016-11-04 13:00:00"=6, "2016-11-04 15:00:00"=6

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| session | 9afaf87c | 989004ea | 989004ea |
| user_id | U002 | U001 | U001 |
| action | purchase | view | add_cart |
| category | drama | null | drama |
| products | D002 | null | D001 |
| amount | 1000 | null | null |
| stamp | 2016-11-04 13:00:00 | 2016-11-03 18:00:00 | 2016-11-03 18:00:00 |

# "action_log_with_ip"  (rows=12)

columns:
"session" varchar255: "0CVKaz"=1, "111f2996"=1, "1QceiB"=1, "1cf7678e"=1, "1hI43A"=1, "3efe001c"=1, "47db0370"=1, "5d5b0997"=1, "5eb2e107"=1, "87b5725f"=1, "989004ea"=1, "fe05e1d8"=1
"user_id" varchar255: "U001"=3, "U002"=2, "U003"=2, "U004"=1, "U005"=1, "U006"=1, "U007"=1, "U008"=1
"action" varchar255: "view"=12
"ip" varchar255: "216.58.220.238"=3, "210.154.149.63"=2, "98.139.183.24"=2, "10.0.0.3"=1, "127.0.0.1"=1, "172.16.0.5"=1, "192.0.0.10"=1, "192.168.0.23"=1
"stamp" varchar255: "2016-11-03 18:00:00"=2, "2016-11-03 19:00:00"=2, "2016-11-03 20:00:00"=2, "2016-11-03 21:00:00"=1, "2016-11-04 18:00:00"=1, "2016-11-04 19:00:00"=1, "2016-11-04 20:00:00"=1, "2016-11-04 21:00:00"=1, "2016-11-04 22:00:00"=1

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| session | fe05e1d8 | 1cf7678e | 1QceiB |
| user_id | U001 | U003 | U002 |
| action | view | view | view |
| ip | 216.58.220.238 | 210.154.149.63 | 98.139.183.24 |
| stamp | 2016-11-04 18:00:00 | 2016-11-03 20:00:00 | 2016-11-03 19:00:00 |

# "activity_log"  (rows=244)

columns:
"stamp" varchar255: iso-date, 21 distinct
"session" varchar255: "87b5725f"=49, "9afaf87c"=33, "111f2996"=28, "8cc03a54"=22, "989004ea"=21, "1cf7678e"=14, "36dd0df7"=14, "0fe39581"=7, "3efe001c"=7, "47db0370"=7, "5d5b0997"=7, "5eb2e107"=7, "cabf98e8"=7, "d45ec190"=7, "eee2bb21"=7, "fe05e1d8"=7
"action" varchar255: "view"=244
"option" varchar255: "page"=93, "detail"=79, "search"=72
"path" varchar255: "/detail"=55, "/search_list"=50, "/search_input"=25, "/detail/"=24, "/search_list/"=22, "/"=16, ""=12, "/complete"=10, "/confirm"=10, "/input"=10, "/search_input/"=10
"search_type" varchar255: ""=164, "Area-L"=22, "Area-S"=14, "Pref"=14, "Area-L-with-Job"=7, "Line"=7, "Pref-with-Job"=7, "Station-with-Job"=7, "Line-with-Job"=2

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| stamp | 2017-01-09 12:25:25 | 2017-01-09 12:18:43 | 2017-01-09 12:18:45 |
| session | 87b5725f | 1cf7678e | 8cc03a54 |
| action | view | view | view |
| option | page | detail | page |
| path | / | /detail/ | /confirm |
| search_type |  |  | Area-L |

# "app1_mst_users"  (rows=2)

columns:
"user_id" varchar255: unique identifier
"name" varchar255: "Sato"=1, "Suzuki"=1
"email" varchar255: "sato@example.com"=1, "suzuki@example.com"=1

indexes: none
fk: none

all rows:
| column | row 1 | row 2 |
|---|---|---|
| user_id | U001 | U002 |
| name | Sato | Suzuki |
| email | sato@example.com | suzuki@example.com |

# "app2_mst_users"  (rows=2)

columns:
"user_id" varchar255: unique identifier
"name" varchar255: "Ito"=1, "Tanaka"=1
"phone" varchar255: "070-xxxx-xxxx"=1, "080-xxxx-xxxx"=1

indexes: none
fk: none

all rows:
| column | row 1 | row 2 |
|---|---|---|
| user_id | U001 | U002 |
| name | Ito | Tanaka |
| phone | 080-xxxx-xxxx | 070-xxxx-xxxx |

# "dup_action_log"  (rows=11)

columns:
"stamp" varchar255: "2016-11-03 21:00:00"=2, "2016-11-03 18:00:00"=1, "2016-11-03 19:00:00"=1, "2016-11-03 20:00:00"=1, "2016-11-04 18:00:00"=1, "2016-11-04 19:00:00"=1, "2016-11-04 20:00:00"=1, "2016-11-04 21:00:00"=1, "2016-11-04 22:00:00"=1, "2016-11-04 22:00:10"=1
"session" varchar255: "3efe001c"=2, "111f2996"=1, "1cf7678e"=1, "47db0370"=1, "5d5b0997"=1, "5eb2e107"=1, "87b5725f"=1, "989004ea"=1, "eee2bb21"=1, "fe05e1d8"=1
"user_id" varchar255: "U001"=2, "U004"=2, "U008"=2, "U002"=1, "U003"=1, "U005"=1, "U006"=1, "U007"=1
"action" varchar255: "click"=11
"products" varchar255: "A001"=5, "D001"=4, "D002"=2

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| stamp | 2016-11-04 22:00:10 | 2016-11-03 18:00:00 | 2016-11-03 19:00:00 |
| session | 3efe001c | 989004ea | 47db0370 |
| user_id | U008 | U001 | U002 |
| action | click | click | click |
| products | A001 | D001 | D002 |

# "form_error_log"  (rows=8)

columns:
"stamp" varchar255: "2016-12-30 00:56:08"=3, "2016-12-30 00:56:09"=3, "2016-12-30 00:56:42"=1, "2016-12-30 00:57:21"=1
"session" varchar255: "004dc3ef"=3, "01061716"=2, "00700be4"=1, "02596e8a"=1, "035a1ebb"=1
"form" varchar255: "regist"=6, "cart"=2
"field" varchar255: "email"=3, "kana"=3, "tel"=1, "zip"=1
"error_type" varchar255: "format_error"=4, "require"=3, "not_kana"=1
"value" varchar255: ""=3, "03-99999999"=1, "101-"=1, "xxx---.co.jp"=1, "xxx@---cojp"=1, "山田 太郎"=1

indexes: none
fk: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 |
|---|---|---|---|---|---|---|---|---|
| stamp | 2016-12-30 00:56:08 | 2016-12-30 00:56:08 | 2016-12-30 00:56:08 | 2016-12-30 00:56:09 | 2016-12-30 00:56:09 | 2016-12-30 00:56:09 | 2016-12-30 00:56:42 | 2016-12-30 00:57:21 |
| session | 004dc3ef | 004dc3ef | 00700be4 | 01061716 | 02596e8a | 035a1ebb | 01061716 | 004dc3ef |
| form | regist | regist | cart | regist | regist | cart | regist | regist |
| field | email | kana | email | email | kana | tel | kana | zip |
| error_type | require | require | format_error | format_error | require | format_error | not_kana | format_error |
| value |  |  | xxx---.co.jp | xxx@---cojp |  | 03-99999999 | 山田 太郎 | 101- |

# "form_log"  (rows=45)

columns:
"stamp" varchar255: "2016-12-30 00:56:08"=21, "2016-12-30 00:57:04"=3, "2016-12-30 00:57:31"=3, "2016-12-30 00:57:48"=3, "2016-12-30 00:57:56"=3, "2016-12-30 00:58:50"=3, "2016-12-30 00:58:58"=3, "2016-12-30 01:00:06"=3, "2016-12-30 01:00:19"=3
"session" varchar255: "9b5f320f"=15, "b2dbcc54"=12, "46b4c72c"=6, "42532886"=3, "539eb753"=3, "647219c7"=3, "8e9afadc"=3
"action" varchar255: "view"=45
"path" varchar255: "/regist/confirm"=15, "/contact/input"=12, "/contact/confirm"=6, "/regist/input"=6, "/cart/input"=3, "/contact/complete"=3
"status" varchar255: ""=30, "error"=15

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| stamp | 2016-12-30 01:00:19 | 2016-12-30 00:58:58 | 2016-12-30 00:56:08 |
| session | 9b5f320f | b2dbcc54 | 8e9afadc |
| action | view | view | view |
| path | /regist/confirm | /contact/confirm | /contact/input |
| status | error |  |  |

# "invalid_action_log"  (rows=7)

columns:
"stamp" varchar255: "2016-11-03 18:00:00"=2, "2016-11-03 18:01:00"=1, "2016-11-03 18:02:00"=1, "2016-11-03 18:10:00"=1, "2016-11-04 13:00:00"=1, nulls=1
"session" varchar255: "0CVKaz"=5, "1QceiB"=2
"user_id" varchar255: "U001"=5, "U002"=2
"action" varchar255: "purchase"=3, "add_cart"=2, "favorite"=1, "view"=1
"category" varchar255: "drama"=5, "action"=1, nulls=1
"products" varchar255: "D002"=2, "A005,A006"=1, "D001"=1, "D001,D002"=1, nulls=2
"amount" int: 1000=2, 2000=1, nulls=4

indexes: none
fk: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 |
|---|---|---|---|---|---|---|---|
| stamp | null | 2016-11-03 18:00:00 | 2016-11-03 18:00:00 | 2016-11-03 18:01:00 | 2016-11-03 18:02:00 | 2016-11-03 18:10:00 | 2016-11-04 13:00:00 |
| session | 1QceiB | 0CVKaz | 0CVKaz | 0CVKaz | 0CVKaz | 0CVKaz | 1QceiB |
| user_id | U002 | U001 | U001 | U001 | U001 | U001 | U002 |
| action | purchase | favorite | view | add_cart | add_cart | purchase | purchase |
| category | action | drama | null | drama | drama | drama | drama |
| products | A005,A006 | D001 | null | D002 | null | D001,D002 | D002 |
| amount | 1000 | null | null | null | null | 2000 | 1000 |

# "mst_categories"  (rows=8)

columns:
"id" int: 6=2, 1=1, 2=1, 3=1, 4=1, 5=1, 7=1, 1..7
"name" varchar255: "book"=1, "cooking"=1, "dvd"=1, "food"=1, "game"=1, "ladys_fashion"=1, "mens_fashion"=1, "supplement"=1
"stamp" varchar255: "2016-01-01 10:00:00"=7, "2016-02-01 10:00:00"=1

indexes: none
fk: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 |
|---|---|---|---|---|---|---|---|---|
| id | 1 | 2 | 3 | 4 | 5 | 6 | 6 | 7 |
| name | ladys_fashion | mens_fashion | book | game | dvd | cooking | food | supplement |
| stamp | 2016-01-01 10:00:00 | 2016-01-01 10:00:00 | 2016-01-01 10:00:00 | 2016-01-01 10:00:00 | 2016-01-01 10:00:00 | 2016-02-01 10:00:00 | 2016-01-01 10:00:00 | 2016-01-01 10:00:00 |

# "mst_products_20161201"  (rows=6)

columns:
"product_id" varchar255: unique identifier
"name" varchar255: "AAA"=1, "AAB"=1, "BBB"=1, "BBD"=1, "CCA"=1, "DAA"=1
"price" int: 3000=2, 4000=2, 5000=2, 3000..5000
"updated_at" varchar255: "2016-11-03 18:00:00"=1, "2016-11-03 19:00:00"=1, "2016-11-03 20:00:00"=1, "2016-11-03 21:00:00"=1, "2016-11-04 18:00:00"=1, "2016-11-04 19:00:00"=1

indexes: none
fk: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 |
|---|---|---|---|---|---|---|
| product_id | A001 | A002 | B001 | B002 | C001 | D001 |
| name | AAA | AAB | BBB | BBD | CCA | DAA |
| price | 3000 | 4000 | 5000 | 3000 | 4000 | 5000 |
| updated_at | 2016-11-03 18:00:00 | 2016-11-03 19:00:00 | 2016-11-03 20:00:00 | 2016-11-03 21:00:00 | 2016-11-04 18:00:00 | 2016-11-04 19:00:00 |

# "mst_products_20170101"  (rows=6)

columns:
"product_id" varchar255: unique identifier
"name" varchar255: "AAA"=1, "AAB"=1, "BBD"=1, "CCA"=1, "DAA"=1, "DAD"=1
"price" int: 5000=3, 3000=2, 4000=1, 3000..5000
"updated_at" varchar255: "2016-11-03 18:00:00"=1, "2016-11-03 19:00:00"=1, "2016-11-03 21:00:00"=1, "2016-11-04 19:00:00"=1, "2016-12-04 18:00:00"=1, "2016-12-04 19:00:00"=1

indexes: none
fk: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 |
|---|---|---|---|---|---|---|
| product_id | A001 | A002 | B002 | C001 | D001 | D002 |
| name | AAA | AAB | BBD | CCA | DAA | DAD |
| price | 3000 | 4000 | 3000 | 5000 | 5000 | 5000 |
| updated_at | 2016-11-03 18:00:00 | 2016-11-03 19:00:00 | 2016-11-03 21:00:00 | 2016-12-04 18:00:00 | 2016-11-04 19:00:00 | 2016-12-04 19:00:00 |

# "mst_users"  (rows=320)

columns:
"user_id" varchar255: 30 distinct
"sex" varchar255: "F"=168, "M"=152
"birth_date" varchar255: iso-date, 30 distinct
"register_date" varchar255: "2016-10-01"=160, "2016-10-02"=77, "2016-10-10"=27, "2016-10-05"=18, "2016-10-15"=9, "2016-10-16"=9, "2016-11-01"=5, "2016-11-03"=3, "2016-10-18"=2, "2016-11-05"=2, "2016-11-10"=2, "2016-11-28"=2, "2016-10-20"=1, "2016-10-25"=1, "2016-11-04"=1, "2016-11-15"=1
"register_device" varchar255: "pc"=136, "app"=96, "sp"=88
"withdraw_date" varchar255: "2016-10-10"=32, nulls=288

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| user_id | U030 | U018 | U015 |
| sex | M | M | F |
| birth_date | 1959-10-07 | 2009-10-12 | 1994-03-01 |
| register_date | 2016-11-28 | 2016-11-01 | 2016-10-01 |
| register_device | sp | app | app |
| withdraw_date | null | null | null |

# "mst_users_with_card_number"  (rows=3)

columns:
"user_id" varchar255: unique identifier
"card_number" varchar255: "1234-xxxx-xxxx-xxxx"=1, "5678-xxxx-xxxx-xxxx"=1, nulls=1

indexes: none
fk: none

all rows:
| column | row 1 | row 2 | row 3 |
|---|---|---|---|
| user_id | U001 | U002 | U003 |
| card_number | 1234-xxxx-xxxx-xxxx | null | 5678-xxxx-xxxx-xxxx |

# "product_sales"  (rows=10)

columns:
"category_name" varchar255: "book"=4, "cd"=3, "dvd"=3
"product_id" varchar255: unique identifier
"sales" int: 10000=3, 20000=3, 5000=1, 15000=1, 30000=1, 50000=1, 5000..50000

indexes: none
fk: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 | row 9 | row 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| category_name | book | book | book | book | cd | cd | cd | dvd | dvd | dvd |
| product_id | B001 | B002 | B003 | B004 | C001 | C002 | C003 | D001 | D002 | D003 |
| sales | 20000 | 15000 | 10000 | 5000 | 30000 | 20000 | 10000 | 50000 | 20000 | 10000 |

# "purchase_log"  (rows=5)

columns:
"purchase_id" int: unique identifier, 10001..10005
"user_id" varchar255: "U001"=3, "U002"=2
"amount" int: 200=2, 400=1, 500=1, 800=1, 200..800
"stamp" varchar255: "2017-01-30 10:00:00"=1, "2017-02-10 10:00:00"=1, "2017-02-12 10:00:00"=1, "2017-03-01 10:00:00"=1, "2017-03-02 10:00:00"=1

indexes: none
fk: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 |
|---|---|---|---|---|---|
| purchase_id | 10001 | 10002 | 10003 | 10004 | 10005 |
| user_id | U001 | U001 | U001 | U002 | U002 |
| amount | 200 | 500 | 200 | 800 | 400 |
| stamp | 2017-01-30 10:00:00 | 2017-02-10 10:00:00 | 2017-02-12 10:00:00 | 2017-03-01 10:00:00 | 2017-03-02 10:00:00 |

# "read_log"  (rows=15)

columns:
"stamp" varchar255: "2016-12-29 21:45:47"=6, "2016-12-29 21:45:49"=1, "2016-12-29 21:45:54"=1, "2016-12-29 21:45:56"=1, "2016-12-29 21:45:59"=1, "2016-12-29 21:46:05"=1, "2016-12-29 21:46:08"=1, "2016-12-29 21:46:13"=1, "2016-12-29 21:46:22"=1, "2016-12-29 21:46:25"=1
"session" varchar255: "df6eb25d"=6, "76c67c39"=4, "77d477cc"=2, "08962ace"=1, "a80ded24"=1, "afbd3d09"=1
"action" varchar255: "view"=6, "read-20%"=3, "read-40%"=2, "read-60%"=2, "read-100%"=1, "read-80%"=1
"url" varchar255: "http://www.example.com/article?id=news731"=6, "http://www.example.com/article?id=trend925"=5, "http://www.example.com/article?id=it605"=2, "http://www.example.com/article?id=news341"=1, "http://www.example.com/article?id=trend132"=1

indexes: none
fk: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| stamp | 2016-12-29 21:46:25 | 2016-12-29 21:45:56 | 2016-12-29 21:45:47 |
| session | df6eb25d | df6eb25d | a80ded24 |
| action | read-100% | read-20% | view |
| url | http://www.example.com/article?id=news731 | http://www.example.com/article?id=news731 | http://www.example.com/article?id=trend925 |

- Skipped 1 empty table(s): "action_log_with_noise"
