---
type: protein-evaluation
gene: "CCDC51"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## CCDC51 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CCDC51 |
| 蛋白名称 | Mitochondrial potassium channel |
| 蛋白大小 | 411 aa / 45.8 kDa |
| UniProt ID | Q96ER9 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Centrosome; Mitochondria; Nucleoplasm (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 411 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=6 |
| 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=69.1; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | CCDC51 |
| PPI | 6/10 | ×3 | 18.0 | PPI degree=75 |
| **加权总分** | | | **132/180** | |
| **归一化总分** | | | **73.2/100** | 互证: +2 |

### 3. 分析
- Centrosome; Mitochondria; Nucleoplasm (Supported)
- PubMed strict=6 broad=9
- AF pLDDT=69.1 PDB=0
- InterPro: CCDC51
- Pfam: 
- PPI degree=75 ChIP: None
39718510: Functionally conserved inner mitochondrial membrane proteins CCDC51 and Mdm33 de | 29523688: Proteomics reveals novel protein associations with early endosomes in an epiderm | 34360642: Mutated CCDC51 Coding for a Mitochondrial Protein, MITOK Is a Candidate Gene Def

### 4. 总体评价
**73.2/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Mitochondrial potassium channel

**功能**: Pore-forming subunit of the mitochondrial ATP-gated potassium channel (mitoK(ATP)) (PubMed:31435016). Together with ATP-binding subunit ABCB8/MITOSUR of the mitoK(ATP) channel, mediates ATP-dependent K(+) currents across the mitochondrial inner membrane (PubMed:31435016). An increase in ATP intracellular levels closes the channel, inhibiting K(+) transport, whereas a decrease in ATP levels enhances K(+) uptake in the mitochondrial matrix. May contribute to the homeostatic control of cellular met

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR037660 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CFTR | BioGRID | 0 |
| MOV10 | BioGRID | 0 |
| NXF1 | BioGRID | 0 |
| CEACAM21 | BioGRID | 0 |
| JUP | BioGRID | 0 |
| NEFH | BioGRID | 0 |
| TGM1 | BioGRID | 0 |
| IGHG1 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q96ER9-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000164051-CCDC51

![](https://images.proteinatlas.org/10980/108_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/10980/108_D5_2_red_green.jpg)
![](https://images.proteinatlas.org/10980/85_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/10980/85_D5_2_red_green.jpg)
![](https://images.proteinatlas.org/10980/87_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/10980/87_D5_2_red_green.jpg)
![](https://images.proteinatlas.org/11408/89_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/11408/89_D5_2_red_green.jpg)

### PubMed 文献

**PubMed count: 9**

| 41910839 | MitoQ Triggers Mitochondrial Collapse and Apoptotic Death in Glioblastoma Associated with KATP Channel Expression Change | Neurochem Res 2026 |
| 39718510 | Functionally conserved inner mitochondrial membrane proteins CCDC51 and Mdm33 demarcate a subset of fission events. | J Cell Biol 2025 |
| 38562768 | Human CCDC51 and yeast Mdm33 are functionally conserved mitochondrial inner membrane proteins that demarcate a subset of | bioRxiv 2024 |

### 深度机制分析

CCDC51（也称MITOK）的域架构由卷曲螺旋（coiled-coil）二聚化模块主导（IPR037660）。411个残基（45.8 kDa）折叠为以两亲性α-螺旋卷曲螺旋为主的结构，插入线粒体内膜，C端面向膜间空间，N端面向基质。该蛋白被描述为线粒体钾通道（mitoK(ATP)）的成孔亚基，通过与ATP结合亚基ABCB8/MITOSUR形成异源复合物介导线粒体基质对ATP敏感的K⁺摄取（PMID 31435016）。

AlphaFold pLDDT为中等水平（69.1），卷曲螺旋骨架可能正常折叠，但连接环和跨膜片段可能偏离典型构象。无实验PDB数据。mitoK(ATP)通道是动态的——高ATP水平促进闭合构象，低ATP则诱导开放构象，两种状态可能差异显著。PPI网络（degree=75）中CFTR和NXF1（核RNA输出因子）的互作具有提示性，MOV10（一种RNA解旋酶）的连接暗示可能的核糖核蛋白复合物参与。

核质定位（HPA Supported, 8/10）与经典核编码线粒体蛋白形成对比。这可能表明蛋白质的双重靶向——一些蛋白质具有模糊的拓扑信号，可同时靶向线粒体和核质。另一种可能是HPA中检测到的核质定位反映的是尚未完成线粒体导入的新合成蛋白池，或从线粒体释放出的切割片段。线粒体与核之间的逆行信号通路已是广为人知的事实，CCDC51核质池可能充当ATP状态的代谢传感器。

TE调控启示：转座子激活事件通常会损害线粒体功能并增加ROS负荷——mitoK(ATP)通道活性则通过轻度解偶联保护线粒体。CCDC51作为线粒体保护性因子可能间接维持TE激活细胞中的基因组稳定性。其母系功能保守性（酵母Mdm33在裂变中的作用得以保留，PMID 39718510）意味着其生化角色是古老而坚固的。6篇文献的极高新颖性为探索线粒体-TE串扰提供了广阔的创新空间。


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CCDC51

