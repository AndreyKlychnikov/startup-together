export interface IUserProfile {
    email: string;
    is_active: boolean;
    is_superuser: boolean;
    full_name: string;
    id: number;
}

export interface IUserProfileUpdate {
    email?: string;
    full_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
}

export interface IUserProfileCreate {
    email: string;
    full_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
}

export interface IProjectItem {
    title: string;
    description: string;
    id: number;
    owner_id: number;
    members: [
        {
            user: {
                email: string;
                is_active: boolean;
                is_superuser: boolean;
                full_name: string;
                id: number;
            },
            accepted: boolean;
        }
    ]
}
