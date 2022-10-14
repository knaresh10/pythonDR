#include<stdio.h>
#include<stdlib.h>
struct Node
{
	int data;
	struct Node *add;	
};
typedef struct Node NODE;
NODE *Head=NULL;

void insert_end(int data)
{
	NODE *NN,*temp;
	NN=(NODE *)malloc(sizeof(NODE));
	NN->data=data;
	NN->add=NULL;
	if(Head==NULL)
	{
		Head=NN;
	}
	else
	{
		temp=Head;
		while(temp->add!=NULL)
		{
			temp=temp->add;
		}
		temp->add=NN;
	}
}
void display()
{
	NODE *temp;
	if(Head==NULL)
	{
		printf("No Nodes\n");
	}
	else
	{
		temp=Head;
		while(temp!=NULL)
		{
			//printf("%d %d %d\n",temp,temp->data,temp->add);
			printf("%d ",temp->data);
			temp=temp->add;
		}
		printf("\n");
	}
}

int delete_end()
{
	//3
	int val;
	NODE *temp;
	if(Head==NULL)
	{
		return -1;
	}
	else if(Head->add==NULL)
	{
		val=Head->data;
		Head=NULL;
		return val;
	}
	else
	{
		temp=Head;
		while(temp->add->add)//
		{
			temp=temp->add;
		}
		val=temp->add->data;
		temp->add=NULL;
		return val;
	}
}
void insert_head(int data)
{
	NODE *NN;
	NN=(NODE *)malloc(sizeof(NODE));
	NN->data=data;
	NN->add=NULL;
	if(Head==NULL)
	{
		Head=NN;
	}
	else
	{
		NN->add=Head;
		Head=NN;
	}
}
int delete_head()
{
	NODE *temp;
	if(Head==NULL)
	{
		return -1;
	}
	else
	{
		temp=Head;
		Head=Head->add;
		temp->add=NULL;
		return temp->data;
	}
}
void insert_pos(int val,int pos)
{
	NODE *nn,*temp;
	int cn=1,i,f=0;
	nn=(NODE *)malloc(sizeof(NODE));
	nn->data=val;
	nn->add=NULL;
	temp=Head;
	while(temp)
	{
		temp=temp->add;
		cn++;
	}
	if(Head==NULL)
	{
		Head=nn;
	}
	else if(pos==1)
	{
		insert_head(val);
	}
	else if(pos>cn)
	{
		insert_end(val);
	}
	else
	{
		temp=Head;
		for(i=1;i<pos-1;i++)
		{
			temp=temp->add;
		}
		nn->add=temp->add;
		temp->add=nn;
		
	}
}
int delete_pos(int pos)
{
	int i=1,cn=1,val;
	NODE *temp=Head;
	while(temp)
	{
		temp=temp->add;
		cn++;
	}
	if(Head==NULL)
	{
		return -1;
	}
	else if(Head->add==NULL)
	{
		val=Head->data;
		Head=NULL;
		return val;
	}
	else if(pos==1)
	{
		val=delete_head();
		return val;
	}
	else if(pos>cn)
	{
		val=delete_end();
		return val;
	}
	else
	{
		temp=Head;
		for(i=1;i<pos-1;i++)
		{
			temp=temp->add;
		}
		val=temp->add->data;
		temp->add=temp->add->add;
		return val;
	}
}
void main()
{
	int ch,data,pos;
	while(1)
	{
		printf("1.insert at end 2.delete at end 3. insert at head 4. delete at head 5.display 6.insert by pos 7.delete by pos 6.exit");
		scanf("%d",&ch);
		if(ch==1)
		{
			//insert data
			scanf("%d",&data);
			insert_end(data);
		}
		else if(ch==2)
		{
			//delete node
			data=delete_end();//
			if(data==-1)
			{
				printf("no nodes\n");
			}
			else
			{
				printf("%d\n",data);//
			}			
		}
		else if(ch==3)
		{
			//insert at head
			scanf("%d",&data);
			insert_head(data);
		}
		else if(ch==4)
		{
			//delete at head
			data=delete_head();
			if(data==-1)
			{
				printf("no nodes\n");
			}
			else
			{
				printf("%d\n",data);//
			}	
			
		}
		else if(ch==5)
		{
			//display data
			display();
		}
		else if(ch==6)
		{
			//insert by pos
			scanf("%d%d",&data,&pos);
			insert_pos(data,pos);
		}
		else if(ch==7)
		{
			//delete by pos
			scanf("%d",&pos);
			data=delete_pos(pos);
			if(data==-1)
			{
				printf("NO Nodes\n");
			}
			else
			{
				printf("%d\n",data);
			}
		}
		else
		{
			break;
		}
	}
}

/*
insert head   
insert end   

delete head
delete end 

dis
*/



























