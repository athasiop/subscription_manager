create user 'admin'@'localhost' identified by 'admin';
grant all privileges on subscription_manager.* to 'admin'@'localhost';

create user 'user'@'%' identified by 'pass';
grant select on subscription_manager.* to 'user'@'%';
grant insert,update,delete on subscription_manager.user to 'user'@'%';
grant insert,delete,update on subscription_manager.payment_method to 'user'@'%';
grant insert,update,delete on subscription_manager.wallet to 'user'@'%';
grant insert,update,delete on subscription_manager.support_ticket to 'user'@'%';
grant insert,delete,update on subscription_manager.user_reviews_service to 'user'@'%';
grant insert,update,delete on subscription_manager.user_buys_subscription_plan to 'user'@'%';
grant insert,update,delete on subscription_manager.user_buys_bundle to 'user'@'%';


create user 'techSupport'@'%' identified by 'techsup';
grant select on subscription_manager.* to 'techSupport'@'%';
grant delete,update on subscription_manager.user to 'techSupport'@'%';
grant update on subscription_manager.payment_method to 'techSupport'@'%';
grant update on subscription_manager.wallet to 'techSupport'@'%';
grant update on subscription_manager.support_ticket to 'techSupport'@'%';
grant insert,update,delete on subscription_manager.user_buys_subscription_plan to 'techSupport'@'%';
grant insert,update,delete on subscription_manager.user_buys_bundle to 'techSupport'@'%';

create user 'company'@'%' identified by 'comp';
grant select on subscription_manager.user to 'company'@'%';
grant select on subscription_manager.user_reviews_service to 'company'@'%';
grant select on subscription_manager.bundle to 'company'@'%';
grant select on subscription_manager.bundle_contains_subscription_plan to 'company'@'%';
grant select on subscription_manager.subscription_service to 'company'@'%';
grant select,insert,update,delete on subscription_manager.subscription_plan to 'company'@'%';
grant select on subscription_manager.user_buys_subscription_plan to 'company'@'%';
grant select on subscription_manager.user_buys_bundle to 'company'@'%';

