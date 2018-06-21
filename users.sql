PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE user (
	id INTEGER NOT NULL, 
	username VARCHAR(64), 
	email VARCHAR(24), 
	password_hash VARCHAR(128), about_me VARCHAR(140), last_seen DATETIME, 
	PRIMARY KEY (id)
);
INSERT INTO user VALUES(1,'susan','susan@e.com','pbkdf2:sha256:50000$aGKYPY2I$aa7e04807c3e3aaa210f7c6ce1fcbdc41e674363bc28363a0064647613219f13',NULL,'2018-06-06 16:24:00.573828');
INSERT INTO user VALUES(2,'moo','m@m.com','pbkdf2:sha256:50000$T8SVUKPW$150978474cc37759dff21087f82a4a723dd545699d22b95f381c90c02d54598b',NULL,'2018-06-03 18:39:09.296948');
INSERT INTO user VALUES(3,'z','z@z.com','pbkdf2:sha256:50000$SvhtJQWQ$be0b9ec4262c7e09bf0d2ce3abd00855fadb78db5156c7b649d09326dca5d24b',NULL,NULL);
INSERT INTO user VALUES(4,'jane','jane@j.com','pbkdf2:sha256:50000$CVLwhAEg$bfeeb896d19dafbb54c63a4c781270609e34fa2bbc2e8fb1380c3d6b20319134',NULL,'2018-06-05 02:42:08.932778');
INSERT INTO user VALUES(5,'joe','joe@joe.com','pbkdf2:sha256:50000$LYg9mFYC$a0a1c7c705ba34b4ccda0e39a46c33c67a8f667e2e78598f7e3d80cb4868a8d2','I am Joe!!! I hate Volcanoes','2018-06-18 13:56:39.831588');
INSERT INTO user VALUES(6,'jack','j@ja.com','pbkdf2:sha256:50000$jv22TAfo$a16db2ce195081c218c63a2a9f91c523b09fc8b4ad2ceecab9043182b7ae6f5f','I love the sun.','2018-06-20 10:15:27.448277');
INSERT INTO user VALUES(7,'gob','gob@gob.com','pbkdf2:sha256:50000$M1FHJ9i3$abfcb61cb02768bab3a2b04e4b8f725f07552acede87333345245747f92fbae9',NULL,'2018-06-03 17:02:05.819937');
INSERT INTO user VALUES(8,'jill','jill@jill.com','pbkdf2:sha256:50000$26UWm6Ja$382d60bbb3a47e4c5e3e89ecca53e579c370d76b95d47775c00da3dfb3fe5114',NULL,'2018-06-19 16:02:03.497589');
CREATE UNIQUE INDEX ix_user_email ON user (email);
CREATE UNIQUE INDEX ix_user_username ON user (username);
COMMIT;
