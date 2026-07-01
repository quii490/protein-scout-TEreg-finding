---
type: protein-evaluation
gene: "CMPK2"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## CMPK2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CMPK2 |
| 蛋白名称 | UMP-CMP kinase 2, mitochondrial |
| 蛋白大小 | 449 aa / 49.4 kDa |
| UniProt ID | Q5EBM0 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Mitochondria; Nucleoplasm (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 449 aa |
| 新颖性 | 7/10 | ×5 | 35.0 | PubMed=95 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=86.6; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | P-loop_NTPase; Thymidylate_kin-like_dom; UMP-CMP_kinase_2 |
| PPI | 6/10 | ×3 | 18.0 | PPI degree=70 |
| **加权总分** | | | **123/180** | |
| **归一化总分** | | | **68.3/100** | 互证: +2 |

### 3. 分析
- Mitochondria; Nucleoplasm (Supported)
- PubMed strict=95 broad=137
- AF pLDDT=86.6 PDB=0
- InterPro: P-loop_NTPase; Thymidylate_kin-like_dom; UMP-CMP_kinase_2
- Pfam: Thymidylate_kin
- PPI degree=70 ChIP: None
34267761: Comparative Proteomic Analysis of Polarized Human THP-1 and Mouse RAW264.7 Macro | 39855350: Hepatocellular CMPK2 promotes the development of metabolic dysfunction-associate | 37339559: Endothelial Gata6 deletion reduces monocyte recruitment and proinflammatory macr

### 4. 总体评价
**68.3/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**线粒体核苷酸激酶的核质救援功能**：CMPK2（UMP-CMP kinase 2, mitochondrial, 449 aa, UniProt Q5EBM0）是线粒体dNTP补救合成途径的关键激酶，催化(d)CMP和(d)UMP的磷酸化产生(d)CDP和(d)UDP（PMID:17999954）。其结构域为P-loop核苷酸激酶超家族（IPR027417）成员，含有一个胸苷酸激酶样结构域（Thymidylate_kin-like_dom IPR039430）和保守的P-loopWalker A/B基序，ATP依赖性磷酸基团转移机制已充分解析。该蛋白也通过IFN依赖和IFN非依赖途径发挥抗病毒免疫调节活性（PMIDs:30083606, 36930652, 37075076）。HPA定位数据显示线粒体和核质双定位（Nucleoplasm Supported, 核定位特异性8/10），推测其可能在线粒体和细胞核之间协调核苷酸代谢。

**dNTP池平衡与TE逆转座的核苷酸供应角色**：LINE-1逆转座需要胞内dNTP作为逆转录底物——逆转录酶（ORF2p）利用宿主细胞的dNTP池合成cDNA。若CMPK2在核质中调节dNTP（特别是dCTP）的局部浓度，可能直接影响L1逆转座在核内的cDNA合成效率。支持这一观点的间接证据包括：核苷酸还原酶（RNR）亚基RRM2在S期与L1 ORF2p发生物理互作，限制dNTP供应用于抑制L1逆转座（PMID:32040502）。然而，从线粒体dNTP补给到核内cDNA合成的调控链条存在多个未验证的生化步骤。

**抗病毒通路与TE免疫的共享信号**：CMPK2通过与Viperin（RSAD2）共同作用限制黄病毒和冠状病毒复制（PMID:36930652, 37075076）。Viperin通过合成ddhCTP（3'-脱氧-3',4'-二脱氢-CTP）作为链终止核苷酸抑制病毒RNA依赖的RNA聚合酶——从概念上，ddhCTP也可能抑制LINE-1逆转录酶的cDNA合成。CMPK2的抗病毒功能可能在先天免疫的TE防御层面具有对等性：IFN/ISG信号激活CMPK2后，通过与Viperin协作（STRING interaction）限制TE逆转座中间体的产生。PPI degree=70中包含DCK（脱氧胞苷激酶, STRING 956）和RRM1（STRING 954），完美构成dNTP代谢酶网络。

**结构质量和新颖性**：AlphaFold pLDDT=86.6的中高置信度和PubMed=95的中等文献量使CMPK2位于领域认知和未知探索的边界。所有95篇文献均集中于抗病毒免疫和嘧啶代谢，无一篇涉及TE调控——但其dNTP代谢酶的身份和抗病毒路径使其成为连接核酸代谢、先天免疫和TE抑制的多功能枢纽蛋白。归一化得分68.3/100的核定位特异性32/40是候选的支撑维度。


### 补充分析 (UniProt API)

**蛋白全称**: UMP-CMP kinase 2, mitochondrial

**功能**: Mitochondrial nucleotide monophosphate kinase needed for salvage dNTP synthesis that mediates immunomodulatory and antiviral activities through IFN-dependent and IFN-independent pathways (PubMed:17999954, PubMed:30083606, PubMed:36930652, PubMed:37075076). Restricts the replication of multiple viruses including flaviviruses or coronaviruses (PubMed:30083606, PubMed:36930652, PubMed:37075076). Together with viperin/RSAD2 and ddhCTP, suppresses the replication of several coronaviruses through inhi

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR027417 |
| InterPro | IPR039430 |
| InterPro | IPR014505 |
| Pfam | PF02223 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| DCK | STRING | 956 |
| RRM1 | STRING | 954 |
| UMPS | STRING | 945 |
| CMPK1 | STRING | 942 |
| UCK2 | STRING | 939 |
| NME7 | STRING | 939 |
| POMP | STRING | 939 |
| NT5C3 | STRING | 939 |