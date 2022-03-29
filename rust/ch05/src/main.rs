#[derive(Debug)]
struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}

fn build_user(email: String, username: String) -> User {
    User {
        email,
        username,
        active: true,
        sign_in_count: 1,
    }
}

#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
}


fn main() {
    let user1 = build_user(String::from("myname@example.com"),String::from("myname"));
    println!("User {} {} ",user1.email,user1.username);
    let scale = 2;
    let rect1 = Rectangle {    
        width: 30,
        height: 50,
    };
    println!("The area of the rectangle is {} square pixels.",
    rect1.area());
}
