INSERT INTO books (
  isbn, title, author, description, category, publisher,
  publication_year, price, stock, image
)
VALUES
  ('9781491950357', 'Designing Data-Intensive Applications', 'Martin Kleppmann', 'Principles and practical techniques for building reliable, scalable, and maintainable data systems.', 'Data Systems', 'O''Reilly Media', 2017, 189900.00, 18, NULL),
  ('9781098115784', 'Designing Machine Learning Systems', 'Chip Huyen', 'An iterative framework for designing production-ready machine learning systems.', 'Machine Learning', 'O''Reilly Media', 2022, 174900.00, 15, NULL),
  ('9781492052203', 'Building Machine Learning Powered Applications', 'Emmanuel Ameisen', 'A practical path from a machine learning idea to a deployed application.', 'Machine Learning', 'O''Reilly Media', 2020, 159900.00, 12, NULL),
  ('9781617294433', 'Machine Learning Engineering', 'Andriy Burkov', 'Engineering principles for building and operating machine learning solutions.', 'Machine Learning', 'Manning', 2020, 149900.00, 10, NULL),
  ('9780132350884', 'Clean Code', 'Robert C. Martin', 'Principles and practices for writing maintainable software.', 'Software Engineering', 'Prentice Hall', 2008, 139900.00, 22, NULL),
  ('9780201616224', 'The Pragmatic Programmer', 'Andrew Hunt and David Thomas', 'Practical approaches to software development and professional engineering.', 'Software Engineering', 'Addison-Wesley', 1999, 129900.00, 16, NULL),
  ('9780131103627', 'The C Programming Language', 'Brian W. Kernighan and Dennis M. Ritchie', 'A concise introduction to the C programming language.', 'Programming', 'Prentice Hall', 1988, 119900.00, 9, NULL),
  ('9780262046305', 'Introduction to Algorithms', 'Thomas H. Cormen et al.', 'A comprehensive reference on algorithms and data structures.', 'Computer Science', 'MIT Press', 2022, 249900.00, 7, NULL),
  ('9781449373320', 'Designing Distributed Systems', 'Brendan Burns', 'Patterns and paradigms for building reliable distributed systems.', 'Distributed Systems', 'O''Reilly Media', 2018, 144900.00, 13, NULL),
  ('9781492078005', 'Fundamentals of Data Engineering', 'Joe Reis and Matt Housley', 'Concepts and practices across the data engineering lifecycle.', 'Data Engineering', 'O''Reilly Media', 2022, 179900.00, 19, NULL),
  ('9781098107963', 'Fundamentals of Software Architecture', 'Mark Richards and Neal Ford', 'An engineering approach to software architecture characteristics and trade-offs.', 'Software Architecture', 'O''Reilly Media', 2020, 169900.00, 14, NULL),
  ('9780134494166', 'Clean Architecture', 'Robert C. Martin', 'Architectural principles for creating maintainable software systems.', 'Software Architecture', 'Pearson', 2017, 154900.00, 11, NULL)
ON CONFLICT (isbn) DO NOTHING;

-- Additional catalog: ISBN, author, publisher and cover verified against Open Library.
INSERT INTO books (
  isbn, title, author, description, category, publisher,
  publication_year, price, stock, image
)
VALUES
  ('9781098125974', 'Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow', 'Aurélien Géron', 'A practical, code-first introduction to building machine learning and deep learning systems.', 'Machine Learning', 'O''Reilly Media', 2022, 134900.00, 15, 'https://covers.openlibrary.org/b/id/15225435-L.jpg'),
  ('9780262035613', 'Deep Learning', 'Ian Goodfellow et al.', 'A comprehensive textbook on the mathematics and methods behind deep neural networks.', 'Machine Learning', 'MIT Press', 2017, 259900.00, 21, 'https://covers.openlibrary.org/b/id/8183675-L.jpg'),
  ('9780387310732', 'Pattern Recognition and Machine Learning', 'Christopher M. Bishop', 'A probabilistic treatment of pattern recognition and machine learning.', 'Machine Learning', 'Springer', 2008, 129900.00, 12, 'https://covers.openlibrary.org/b/id/245089-L.jpg'),
  ('9780262039246', 'Reinforcement Learning: An Introduction', 'Richard S. Sutton and Andrew G. Barto', 'The standard introduction to the ideas and algorithms of reinforcement learning.', 'Machine Learning', 'MIT Press', 2018, 229900.00, 23, 'https://covers.openlibrary.org/b/id/8835517-L.jpg'),
  ('9780134610993', 'Artificial Intelligence: A Modern Approach', 'Stuart J. Russell and Peter Norvig', 'A broad reference on the theory and practice of artificial intelligence.', 'Machine Learning', 'Pearson', 2020, 254900.00, 23, 'https://covers.openlibrary.org/b/id/13530046-L.jpg'),
  ('9780387848570', 'The Elements of Statistical Learning', 'Trevor Hastie, Robert Tibshirani and Jerome Friedman', 'Statistical learning methods for data mining, inference, and prediction.', 'Machine Learning', 'Springer-Verlag New York', 2009, 239900.00, 12, 'https://covers.openlibrary.org/b/id/8643961-L.jpg'),
  ('9781098136796', 'Natural Language Processing with Transformers', 'Lewis Tunstall, Leandro von Werra and Thomas Wolf', 'Building language applications with Hugging Face transformer models.', 'Machine Learning', 'O''Reilly Media', 2022, 99900.00, 24, 'https://covers.openlibrary.org/b/id/13167945-L.jpg'),
  ('9781617293702', 'Grokking Deep Learning', 'Andrew Trask', 'An intuitive, build-it-yourself introduction to deep learning.', 'Machine Learning', 'Manning', 2019, 124900.00, 8, 'https://covers.openlibrary.org/b/id/15236307-L.jpg'),
  ('9781492072942', 'Practical Statistics for Data Scientists', 'Peter Bruce, Andrew Bruce and Peter Gedeck', 'Essential statistical concepts and methods for data science, with examples in R and Python.', 'Machine Learning', 'O''Reilly Media', 2020, 189900.00, 8, 'https://covers.openlibrary.org/b/id/13250986-L.jpg'),
  ('9781491983874', 'Streaming Systems', 'Tyler Akidau, Slava Chernyak and Reuven Lax', 'The what, where, when, and how of large-scale data processing.', 'Data Systems', 'O''Reilly Media', 2018, 239900.00, 5, 'https://covers.openlibrary.org/b/id/8508647-L.jpg'),
  ('9781492040347', 'Database Internals', 'Alex Petrov', 'A deep dive into how distributed data systems work.', 'Data Systems', 'O''Reilly Media', 2019, 254900.00, 15, 'https://covers.openlibrary.org/b/id/14572292-L.jpg'),
  ('9781492043089', 'Kafka: The Definitive Guide', 'Neha Narkhede et al.', 'Real-time data and stream processing at scale with Apache Kafka.', 'Data Systems', 'O''Reilly Media', 2021, 164900.00, 17, 'https://covers.openlibrary.org/b/id/13299527-L.jpg'),
  ('9781680502534', 'Seven Databases in Seven Weeks', 'Luc Perkins, Eric Redmond and Jim Wilson', 'A guide to modern databases and the NoSQL movement.', 'Data Systems', 'Pragmatic Bookshelf', 2018, 179900.00, 16, 'https://covers.openlibrary.org/b/id/8508811-L.jpg'),
  ('9781492080510', 'High Performance MySQL', 'Silvia Botros and Jeremy Tinley', 'Optimization, backups, and replication for MySQL.', 'Data Systems', 'O''Reilly Media', 2022, 209900.00, 17, 'https://covers.openlibrary.org/b/id/13562808-L.jpg'),
  ('9781492087830', 'Data Pipelines Pocket Reference', 'James Densmore', 'Moving and processing data for analytics, in a compact reference.', 'Data Engineering', 'O''Reilly Media', 2021, 259900.00, 25, 'https://covers.openlibrary.org/b/id/10716520-L.jpg'),
  ('9780134757599', 'Refactoring', 'Martin Fowler', 'Improving the design of existing code, in its second edition.', 'Software Engineering', 'Addison-Wesley', 2018, 119900.00, 15, 'https://covers.openlibrary.org/b/id/8507565-L.jpg'),
  ('9780735619678', 'Code Complete', 'Steve McConnell', 'A practical handbook of software construction.', 'Software Engineering', 'Microsoft Press', 2004, 124900.00, 22, 'https://covers.openlibrary.org/b/id/8629368-L.jpg'),
  ('9780131177055', 'Working Effectively with Legacy Code', 'Michael C. Feathers', 'Strategies for changing and testing code that has no tests.', 'Software Engineering', 'Prentice Hall', 2004, 189900.00, 14, 'https://covers.openlibrary.org/b/id/7898496-L.jpg'),
  ('9780201633610', 'Design Patterns', 'Erich Gamma et al.', 'Elements of reusable object-oriented software.', 'Software Engineering', 'Addison-Wesley Professional', 1995, 244900.00, 9, 'https://covers.openlibrary.org/b/id/10827044-L.jpg'),
  ('9780201835953', 'The Mythical Man-Month', 'Frederick P. Brooks', 'Essays on software engineering and project management.', 'Software Engineering', 'Addison-Wesley Professional', 1995, 194900.00, 5, 'https://covers.openlibrary.org/b/id/10653425-L.jpg'),
  ('9781942788331', 'Accelerate', 'Nicole Forsgren, Jez Humble and Gene Kim', 'The science of lean software and DevOps.', 'Software Engineering', 'IT Revolution Press', 2018, 214900.00, 16, 'https://covers.openlibrary.org/b/id/14651184-L.jpg'),
  ('9781732102200', 'A Philosophy of Software Design', 'John K. Ousterhout', 'Principles for reducing complexity in software systems.', 'Software Engineering', 'Yaknyam Press', 2018, 244900.00, 18, 'https://covers.openlibrary.org/b/id/10352230-L.jpg'),
  ('9780321601919', 'Continuous Delivery', 'Jez Humble and David Farley', 'Reliable software releases through build, test, and deployment automation.', 'Software Engineering', 'Addison-Wesley Professional', 2010, 124900.00, 17, 'https://covers.openlibrary.org/b/id/6998977-L.jpg'),
  ('9781680502398', 'Release It!', 'Michael T. Nygard', 'Design and deploy production-ready software.', 'Software Engineering', 'Pragmatic Bookshelf', 2018, 254900.00, 8, 'https://covers.openlibrary.org/b/id/8509030-L.jpg'),
  ('9780135781869', 'Clean Agile', 'Robert C. Martin', 'Back to basics on agile software development.', 'Software Engineering', 'Prentice Hall', 2019, 234900.00, 21, 'https://covers.openlibrary.org/b/id/10222947-L.jpg'),
  ('9781942788294', 'The Phoenix Project', 'Gene Kim, Kevin Behr and George Spafford', 'A novel about IT, DevOps, and helping your business win.', 'Software Engineering', 'IT Revolution Press', 2018, 254900.00, 17, 'https://covers.openlibrary.org/b/id/12391318-L.jpg'),
  ('9780321125217', 'Domain-Driven Design', 'Eric Evans', 'Tackling complexity in the heart of software.', 'Software Architecture', 'Addison-Wesley', 2008, 179900.00, 18, 'https://covers.openlibrary.org/b/id/14596704-L.jpg'),
  ('9781492034025', 'Building Microservices', 'Sam Newman', 'Designing fine-grained systems.', 'Software Architecture', 'O''Reilly Media', 2020, 249900.00, 21, 'https://covers.openlibrary.org/b/id/13165796-L.jpg'),
  ('9781492086895', 'Software Architecture: The Hard Parts', 'Neal Ford et al.', 'Modern trade-off analysis for distributed architectures.', 'Software Architecture', 'O''Reilly Media', 2021, 104900.00, 23, 'https://covers.openlibrary.org/b/id/12318698-L.jpg'),
  ('9780321127426', 'Patterns of Enterprise Application Architecture', 'Martin Fowler', 'A catalog of patterns for enterprise application design.', 'Software Architecture', 'Addison-Wesley', 2007, 169900.00, 9, 'https://covers.openlibrary.org/b/id/14596702-L.jpg'),
  ('9780321200686', 'Enterprise Integration Patterns', 'Gregor Hohpe and Bobby Woolf', 'Designing, building, and deploying messaging solutions.', 'Software Architecture', 'Addison-Wesley', 2008, 114900.00, 21, 'https://covers.openlibrary.org/b/id/14596701-L.jpg'),
  ('9780134685991', 'Effective Java', 'Joshua Bloch', 'Best practices for the Java platform.', 'Programming', 'Addison-Wesley Professional', 2017, 129900.00, 24, 'https://covers.openlibrary.org/b/id/12420356-L.jpg'),
  ('9781492056355', 'Fluent Python', 'Luciano Ramalho', 'Clear, concise, and effective programming in Python.', 'Programming', 'O''Reilly Media', 2021, 234900.00, 20, 'https://covers.openlibrary.org/b/id/10290195-L.jpg'),
  ('9780134190440', 'The Go Programming Language', 'Alan A. A. Donovan and Brian W. Kernighan', 'The authoritative guide to programming in Go.', 'Programming', 'Addison-Wesley', 2016, 144900.00, 20, 'https://covers.openlibrary.org/b/id/7427319-L.jpg'),
  ('9780596517748', 'JavaScript: The Good Parts', 'Douglas Crockford', 'The parts of JavaScript worth using.', 'Programming', 'O''Reilly Media', 2008, 169900.00, 8, 'https://covers.openlibrary.org/b/id/2536428-L.jpg'),
  ('9781718502703', 'Python Crash Course', 'Eric Matthes', 'A hands-on, project-based introduction to programming.', 'Programming', 'No Starch Press', 2022, 244900.00, 20, 'https://covers.openlibrary.org/b/id/15225531-L.jpg'),
  ('9780201657883', 'Programming Pearls', 'Jon Louis Bentley', 'Essays on the craft of programming.', 'Programming', 'Addison-Wesley', 2000, 179900.00, 22, 'https://covers.openlibrary.org/b/id/8112458-L.jpg'),
  ('9780262510875', 'Structure and Interpretation of Computer Programs', 'Harold Abelson, Gerald Jay Sussman and Julie Sussman', 'A classic introduction to computer science through Scheme.', 'Computer Science', 'MIT Press', 1996, 224900.00, 14, 'https://covers.openlibrary.org/b/id/9325174-L.jpg'),
  ('9780134092669', 'Computer Systems: A Programmer''s Perspective', 'Randal E. Bryant and David R. O''Hallaron', 'How hardware and systems software affect program behavior.', 'Computer Science', 'Pearson', 2015, 259900.00, 20, 'https://covers.openlibrary.org/b/id/14858059-L.jpg'),
  ('9781133187790', 'Introduction to the Theory of Computation', 'Michael Sipser', 'Automata, computability, and complexity.', 'Computer Science', 'Cengage Learning', 2013, 224900.00, 18, 'https://covers.openlibrary.org/b/id/14572027-L.jpg'),
  ('9780133591620', 'Modern Operating Systems', 'Andrew S. Tanenbaum and Herbert Bos', 'Principles and design of modern operating systems.', 'Computer Science', 'Pearson', 2015, 159900.00, 14, 'https://covers.openlibrary.org/b/id/7294469-L.jpg'),
  ('9780321573513', 'Algorithms', 'Robert Sedgewick', 'A comprehensive treatment of fundamental algorithms and data structures.', 'Computer Science', 'Addison-Wesley', 2011, 184900.00, 5, 'https://covers.openlibrary.org/b/id/7992499-L.jpg'),
  ('9781617292231', 'Grokking Algorithms', 'Aditya Y. Bhargava', 'An illustrated guide for programmers and other curious people.', 'Computer Science', 'Manning', 2016, 109900.00, 9, 'https://covers.openlibrary.org/b/id/15239913-L.jpg'),
  ('9780201896831', 'The Art of Computer Programming, Volume 1', 'Donald Knuth', 'Fundamental algorithms and mathematical foundations.', 'Computer Science', 'Addison-Wesley', 1997, 244900.00, 21, 'https://covers.openlibrary.org/b/id/136600-L.jpg'),
  ('9780128122754', 'Computer Organization and Design', 'David A. Patterson and John L. Hennessy', 'The hardware/software interface, in its RISC-V edition.', 'Computer Science', 'Morgan Kaufmann', 2017, 254900.00, 16, 'https://covers.openlibrary.org/b/id/10151148-L.jpg'),
  ('9781491929124', 'Site Reliability Engineering', 'Betsy Beyer et al.', 'How Google runs production systems.', 'Distributed Systems', 'O''Reilly Media', 2016, 159900.00, 13, 'https://covers.openlibrary.org/b/id/9196728-L.jpg'),
  ('9781098110208', 'Kubernetes: Up and Running', 'Brendan Burns, Joe Beda and Kelsey Hightower', 'Dive into the future of infrastructure.', 'Distributed Systems', 'O''Reilly Media', 2022, 254900.00, 19, 'https://covers.openlibrary.org/b/id/13512019-L.jpg'),
  ('9781543057386', 'Distributed Systems', 'Andrew S. Tanenbaum, Maarten Van Steen and Maarten van Steen', 'Principles and paradigms of distributed systems.', 'Distributed Systems', 'CreateSpace', 2017, 259900.00, 20, 'https://covers.openlibrary.org/b/id/11158985-L.jpg')
ON CONFLICT (isbn) DO NOTHING;

INSERT INTO customers (
  customer_id, first_name, last_name, email, city, country
)
VALUES
  ('00000000-0000-4000-8000-000000000001', 'Ana', 'Rojas', 'synthetic.customer.0001@bookstore.test', 'Medellín', 'Colombia'),
  ('00000000-0000-4000-8000-000000000002', 'Carlos', 'Gómez', 'synthetic.customer.0002@bookstore.test', 'Bogotá', 'Colombia'),
  ('00000000-0000-4000-8000-000000000003', 'Laura', 'Mejía', 'synthetic.customer.0003@bookstore.test', 'Cali', 'Colombia'),
  ('00000000-0000-4000-8000-000000000004', 'Andrés', 'Restrepo', 'synthetic.customer.0004@bookstore.test', 'Medellín', 'Colombia'),
  ('00000000-0000-4000-8000-000000000005', 'Mariana', 'López', 'synthetic.customer.0005@bookstore.test', 'Barranquilla', 'Colombia'),
  ('00000000-0000-4000-8000-000000000006', 'Santiago', 'Vélez', 'synthetic.customer.0006@bookstore.test', 'Pereira', 'Colombia'),
  ('00000000-0000-4000-8000-000000000007', 'Valentina', 'Ortiz', 'synthetic.customer.0007@bookstore.test', 'Manizales', 'Colombia'),
  ('00000000-0000-4000-8000-000000000008', 'Daniel', 'Ramírez', 'synthetic.customer.0008@bookstore.test', 'Medellín', 'Colombia')
ON CONFLICT DO NOTHING;
