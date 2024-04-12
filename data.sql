BEGIN;


CREATE TABLE IF NOT EXISTS public.expense
(
    userid character varying(50) COLLATE pg_catalog."default",
    date date,
    expense_type character varying(50) COLLATE pg_catalog."default",
    amount numeric(10, 2),
    comment character varying(255) COLLATE pg_catalog."default"
);

CREATE TABLE IF NOT EXISTS public.userinfo
(
    userid character varying(50) COLLATE pg_catalog."default" NOT NULL,
    password character varying(100) COLLATE pg_catalog."default",
    user_name character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT userinfo_pkey PRIMARY KEY (userid)
);

ALTER TABLE IF EXISTS public.expense
    ADD CONSTRAINT expense_userid_fkey FOREIGN KEY (userid)
    REFERENCES public.userinfo (userid) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;

END;