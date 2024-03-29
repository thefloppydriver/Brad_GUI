B
    ��M]�.  �               @   s$  d dl Z d dlZd dlZd dlZd dlZd dlZd dlT d dlmZm	Z	 d dl
mZ d dlmZ dadadad	ad
ddddddd�adae�� ae�� ae�� at�d� t�d� t�d� e�� at�d� e�� ae�� at�d� G dd� de�Ze� Ze� d� ee�Z!t"�  e�#�  dS )�    N)�*)�Image�ImageTk)�EmailMessage)�MIMETextZMelissiaZSPAMMMMzfearmypowergoodsir@gmail.comzsp4m.m3!l   �J� l   /1�= l   W]�= l   AbZ	 l   � �= l   �,�= l   `LiH )ZjomarZjaydenZkendall�ryanZgraceeZrene�adaz�Kendall is on Verizon
Jomar is on T-Mobile
Jayden is on T-Mobile
Kylee is on T-Mobile
Gracee is on AT&T
Rene is on Boost Mobile
I'm on Verizon (Ryan)
Ada is on Verizoni ʚ;�v�   �passFc               @   s�   e Zd Zdad!dd�Zdd� Zdd� Zd	d
� Zdd� Zdd� Z	dd� Z
dd� Zdd� add� Zdd� Zdd� Zdd� Zdd� Zdd � ZdS )"�WindowTNc             C   s   t �| |� || _| ��  d S )N)�Frame�__init__�master�init_window)�selfr   � r   �Brad_GUI.pywr   Z   s    zWindow.__init__c             C   s&  t | jddd�}t | jddd�}t | jddd�}t | jddd�}t| j�at| j�at| j�at| j�at| �}t| ddd	�a	| j�
d
� | jttdd� |jttd� t	jttd� |jt	jd� t	j|jd� t| jd| jd�}t| jd| jd�}t| j�}| jj|d� t|�}	|	jd| jd� |jd|	d� t|�}
|
jd| jd� |
jd| jd� |
jd| jd� |
jd| jd� |
jdd� |jd|
d� |jddd � |jd!dd � |jddd � |jdd!d � |jdd"d � |jdd#d � tjd$dd � tjd$d!d � tjd$d"d � tjd$d#d � d S )%NzNumber or contact:)zCourier New�	   )�textZfontzVictim's carrier:zMessage Delay (s):zWrite to fileMenu:�   �/   )�height�widthzBrad v6.0 with Multi-Threadingr   )�fill�side�expand)r   r   )�command)�yscrollcommandZSPAM)r   r   ZsToP)�menuZExit)�labelr   ZFile)r    r   zShow ContactszEdit message.txtzEdit name.txtzShow notes.txtZUndo)r    ZEdit��   )�x�y�2   �d   �   �   )�Labelr   ZEntry�e1�e2�e3�e4�	Scrollbar�Text�T�title�pack�XZBOTTOM�RIGHT�Y�config�yview�setZButton�update_spamit_thread�stop_spamit_threadZMenuZadd_command�client_exitZadd_cascade�showContacts�editMessage�editName�	showNotesZplace)r   ZnumberOrContactZvictimsCarrierZ	spamDelayZwriteToFileLabel�SZspamitButtonZstopSpammingButtonr   �fileZeditr   r   r   r   e   sP    




zWindow.init_windowc          	   C   s�   t � }t|�}t|ddd�}|jttd� |jttd� |j|jd� |j|j	d� |�
d� ttdd	� t��}|�td
d�tt|�� � t�  d S )N�
   r$   )r   r   )r   r   )r   )r   ZContactsc             S   s   | S )Nr   )r"   r   r   r   �<lambda>�   s    z%Window.showContacts.<locals>.<lambda>zWorking Contacts: 
�
)�Tkr-   r.   r1   r3   r4   �LEFTr5   r6   r7   r0   �list�map�contactstxt�insert�END�join�str�mainloop)r   Znoot�Q�RZbibbyr   r   r   r;   �   s    
zWindow.showContactsc             C   s   t | dd�}|��  d S )NzHey there good lookin!)r   )r(   r1   )r   r   r   r   r   �showText�   s    zWindow.showTextc             C   s,   t �� at�td� t�tdt d � d S )NzMessage updated successfully! 
z	Message: rC   )r,   �get�
messagetxtr/   rI   rJ   )r   r   r   r   r<   �   s    zWindow.editMessagec             C   s,   t �� at�td� t�tdt d � d S )NzName updated successfully! 
zName: rC   )r,   rQ   �nametxtr/   rI   rJ   )r   r   r   r   r=   �   s    zWindow.editNamec          
   C   sf   t �dd�}|��  |�dd� |�dddtt�dd�� d	 d
 d	 d t�	�  d � |�
�  d S )Nzsmtp.gmail.comiK  zfearmypowergoodsir@gmail.comzsp4m.m3!z9809257025@vtext.comzSubject: ALERTr   i'  rC   zTo: , 9809257025@vtext.comzSomeone just tried to spam �.)�smtplib�SMTP�starttls�login�sendmailrL   �random�randintr)   rQ   �quit)r   �sr   r   r   �
alert_ryan�   s
    :zWindow.alert_ryanc             C   st   t � }t|�}t|ddd�}|jttd� |jttd� |j|jd� |j|j	d� |�
d� |�tt� t�  d S )NrA   r$   )r   r   )r   r   )r   )r   ZNotes)rD   r-   r.   r1   r3   r4   rE   r5   r6   r7   r0   rI   rJ   �notestxtrM   )r   Zsoot�C�Dr   r   r   r>   �   s    
zWindow.showNotesc               C   s   t t�� � t�d� d S )Nr   )�exec�executestoragerQ   �putr   r   r   r   �execute�   s    re   c             C   s@  t �� }t �|� |dkr,t �d� td��|dk�r�t|��� dkr�x\y<t|�dksbt|�dkrht�  t|�dkr�t|�dkr�P W qH tk
r�   t�  Y qHX qHW |dks�|dks�|dkr�| �	�  t
��  t�  |}t�td	| � t|��� dk�r�|�� d
k�s|�� dk�rV| �	�  t�td� t�d� t�td� t�d� t
��  t�  yt|��  }W n* tk
�r�   t�t|�� d � Y nX |�� �d��r�d}nz|�� �d��r�d}nd|�� �d��r�d}nN|�� �d��r�d}n8|�� �d��r d}n"|�� �d��rd}nt�td� t� }|�t� t�dd�}tt|� |d< t|d < t|�| |d!< t�d"d#�}	|	��  |	�tt � |	�!tt|�| |�"� � t�td$t|� | d% � |	��  |}
|}|}t �� }t �|� |dk�rt#t$�� � t�t|�� t
�%�  | �&|
||� |dk�r<t�td&� t �d� d S )'NTFZyeetl    d(	 i�ɚ;Z
7049890912l   `LiH Z
9809257025zTarget number:r   r   zoH 
�   zsO tHaT'S hOw It iS NoW 
zJ is not in the list of contacts. (Go tell Ryan, he'll fix it for you :] )
r	   z
@vtext.com�tz@tmomail.net�az@txt.att.netr]   z@messaging.sprintpcs.com�mz@mymetropcs.com�bz@sms.myboostmobile.comzJTHATS NOT A SUPPORTED CARRIER!!! (Go tell Ryan, he'll fix it for you :] )
r   i'  ZSubjectZFromZTozsmtp.gmail.comiK  zSpam message sent to: rC   z
Stopped. 
)'�stop_spammingrQ   rd   �	NameErrorrL   �isdigit�intr\   �
ValueErrorr^   �root�destroyr/   rI   rJ   �lower�time�sleeprH   �KeyError�
startswithr   Zset_contentrR   rZ   r[   rS   �emailtxtrU   rV   rW   rX   �passwordtxtrY   Z	as_string�printr+   �update�spamit)r   �e1get�e2get�e3getZstop_spamminggetZnumberZrealcarrier�msgZthread_numberr]   Ze1get2Ze2get2Ze3get2r   r   r   r{   �   s�    








zWindow.spamitc             C   s.   t j| jt�� t�� t�� fd�at��  d S )N)�target�args)	�	threading�Threadr{   r)   rQ   r*   r+   �spamitthread�start)r   r   r   r   r8   C  s    "zWindow.update_spamit_threadc             C   sj   yt d krt�d� t ��  W nF tk
rd   t�td� t�	�  t
�d� t�td� t�	�  Y nX d S )NTzUhh... 
rf   z...no. 
)r�   rk   rd   rK   rl   r/   rI   rJ   rp   rz   rs   rt   )r   r   r   r   �stopitH  s    

zWindow.stopitc             C   s   t j| jdd�at��  d S )Nr   )r�   r�   )r�   r�   r�   Zstopitthreadr�   )r   r   r   r   r9   W  s    zWindow.stop_spamit_threadc             C   s   t ��  t�  d S )N)rp   rq   r\   )r   r   r   r   r:   ^  s    zWindow.client_exitc             C   s    t �tdt�� t�� f � d S )NzFirst Name: %s
Last Name: %s
)r/   rI   rJ   r)   rQ   r*   )r   r   r   r   �show_entry_fieldsb  s    zWindow.show_entry_fields)N)�__name__�
__module__�__qualname__Zstartttr   r   r;   rP   r<   r=   r^   r>   re   r{   r8   r�   r9   r:   r�   r   r   r   r   r   R   s    
N[r   Z400x300)$rU   rs   rZ   �osr�   ZqueueZtkinterZPILr   r   Zemail.messager   Zemail.mime.textr   rS   rR   rw   rx   rH   r_   ZQueuer|   r}   r~   rd   rc   Z
qspamDelayrk   r   r   rD   rp   ZgeometryZappre   rM   r   r   r   r   �<module>   sP   "




  
