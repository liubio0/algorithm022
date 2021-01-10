class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        1�����⣬˫����ȶԣ�ȡ��С�����ƥ�䡣
        2��˼·��
            1������
            2��ͬʱ��������g��s����������ʱ�����1��ͬʱ�ƶ�(��˫�����)��
            3������������ʱ���ƶ�s��
        3���Ż�˼·��
            ˫��ѭ���еĺͶ����Ż�Ϊ����ѭ����ָ���ƶ���
        """

        s.sort()    #���ɳߴ�
        g.sort()    #С��θ��
        len_s = len(s)
        len_g = len(g)

        i_cookie, i_child = 0, 0

        for i_cookie in range(len_s):
            if i_child > len_g - 1: break
            if s[i_cookie] >= g[i_child]: i_child += 1

        return i_child