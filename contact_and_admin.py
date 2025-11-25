import streamlit as st

def contact_and_admin():
    st.title("Glorious 70 Kingdom")
    st.write("This is our contact and administration page and this will be updated soon.")

    alliances = {
        "THE COUNCIL OF FIRE": {
            "": "",
            "r4_members": [
                {"name": "KING/R5", "role": "THE COUNCIL", "description": " ", "photos": 
                {"name": "Member 3", "role": "Role 3", "description": "Description 3"},
                {"name": "Member 4", "role": "Role 4", "description": "Description 4"},
                {"name": "Member 5", "role": "Role 5", "description": "Description 5"},
                {"name": "Member 6", "role": "Role 6", "description": "Description 6"},
                {"name": "Member 7", "role": "Role 7", "description": "Description 7"},
                {"name": "Member 8", "role": "Role 8", "description": "Description 8"}
            ]
        },
        "THE COUNCIL OF WATER": {
            "logo": "GK70_logo.png",
            "r4_members": [
                {"name": "Member 1", "role": "Role 1", "description": "Description 1"},
                {"name": "Member 2", "role": "Role 2", "description": "Description 2"},
                {"name": "Member 3", "role": "Role 3", "description": "Description 3"},
                {"name": "Member 4", "role": "Role 4", "description": "Description 4"},
                {"name": "Member 5", "role": "Role 5", "description": "Description 5"},
                {"name": "Member 6", "role": "Role 6", "description": "Description 6"},
                {"name": "Member 7", "role": "Role 7", "description": "Description 7"},
                {"name": "Member 8", "role": "Role 8", "description": "Description 8"}
            ]
        },
        "THE COUNCIL OF LIFE": {
            "logo": "GY70_logo.png",
            "r4_members": [
                {"name": "Member 1", "role": "Role 1", "description": "Description 1"},
                {"name": "Member 2", "role": "Role 2", "description": "Description 2"},
                {"name": "Member 3", "role": "Role 3", "description": "Description 3"},
                {"name": "Member 4", "role": "Role 4", "description": "Description 4"},
                {"name": "Member 5", "role": "Role 5", "description": "Description 5"},
                {"name": "Member 6", "role": "Role 6", "description": "Description 6"},
                {"name": "Member 7", "role": "Role 7", "description": "Description 7"},
                {"name": "Member 8", "role": "Role 8", "description": "Description 8"}
            ]
        }
    }

    for alliance, details in alliances.items():
        st.image(details["logo"], caption=f"{alliance} Logo", width=400)
        
        st.markdown(f"### {alliance} R4 Members")
        for i in range(0, len(details["r4_members"]), 2):
            cols = st.columns(2)
            for j in range(2):
                if i + j < len(details["r4_members"]):
                    member = details["r4_members"][i + j]
                    with cols[j]:
                        st.markdown(f"**{member['name']}**")
                        st.markdown(f"*Role*: {member['role']}")
                        st.markdown(f"*Description*: {member['description']}")
                        if 'photos' in member:
                            for photo in member['photos']:
                                st.image(photo, width=200)

if __name__ == "__main__":
    contact_and_admin()
