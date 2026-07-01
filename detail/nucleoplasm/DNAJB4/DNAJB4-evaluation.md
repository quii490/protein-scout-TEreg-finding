---
type: protein-evaluation
gene: "DNAJB4"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## DNAJB4 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | DNAJB4 |
| 蛋白名称 | DnaJ homolog subfamily B member 4 |
| 蛋白大小 | 337 aa / 37.8 kDa |
| UniProt ID | Q9UDY4 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Cytosol; Nucleoplasm; Plasma membrane (Enhanced) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 337 aa |
| 新颖性 | 7/10 | ×5 | 35.0 | PubMed=60 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=82.7; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | DnaJ_C; DnaJ_domain; DnaJ_domain_CS |
| PPI | 7/10 | ×3 | 21.0 | PPI degree=150 |
| **加权总分** | | | **123/180** | |
| **归一化总分** | | | **68.3/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm; Plasma membrane (Enhanced)
- PubMed strict=60 broad=96
- AF pLDDT=82.7 PDB=0
- InterPro: DnaJ_C; DnaJ_domain; DnaJ_domain_CS
- Pfam: DnaJ; DnaJ_C
- PPI degree=150 ChIP: None
36344539: The diagnostic yield, candidate genes, and pitfalls for a genetic study of intel | 36709343: Metamorphism in TDP-43 prion-like domain determines chaperone recognition. | 39468638: Genotype‒phenotype correlation in recessive DNAJB4 myopathy.

### 4. 总体评价
**68.3/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**HSP40/Hsp70伴侣系统的J-域功能与蛋白质量控制**：DNAJB4（DnaJ homolog subfamily B member 4, 337 aa, UniProt Q9UDY4）属于II型DNAJ/HSP40分子伴侣家族，携带N端J结构域（DnaJ_domain IPR001623, Pfam DnaJ）和C端底物结合域（DnaJ_C IPR002939, Pfam DnaJ_C）。J结构域通过保守的HPD三肽基序结合Hsp70的ATPase域，刺激ATP水解并变构耦合底物结合——这一"J-Hsp70偶联"是细胞蛋白质折叠和质量控制的最基本机制。DNAJB4的伴侣功能已被体外实验证实——刺激HSPA1A/B的ATP水解和未折叠蛋白的折叠（PMID:24318877）。DNAJB4的两亲性底物结合域倾向于识别暴露了疏水基团的部分折叠蛋白。

**TDP-43/Prion样结构域的TE蛋白折叠与HSP40防御**：PMID:36709343（Metamorphism in TDP-43 prion-like domain determines chaperone recognition）将DNAJB4拉入神经退行性和TE调控的交叉领域。TDP-43的C端prion样结构域与L1 ORF1p的卷曲螺旋域（CC）在结构折叠和聚集倾向上极为相似——两者均富含甘氨酸和极性氨基酸，采用可逆的cross-β折叠形成同源三聚体。DNAJB4若识别TDP-43的prion样折叠态，同样可能识别L1 ORF1p三聚体并促进其解聚或降解，从而抑制功能性L1 RNP的形成。PMID:39468638（Genotype-phenotype correlation in recessive DNAJB4 myopathy）进一步证实DNAJB4在横纹肌中维持蛋白质稳态的关键性——横纹肌和心肌中LINE-1体细胞逆转座已被检测到。

**HSP70超家族互作网络的TE调控汇聚点**：PPI degree=150（STRING/BioGRID）的丰富互作度反映了DNAJB4作为HSP70网络的J蛋白枢纽。HSPA4（STRING 982）、HSPA1B（STRING 976）、HSPA8/HSC70（STRING 967）和HSPA1A/HSP72（STRING 941）均为已验证的HSP70互作伙伴。特别值得注意的是HSPH1/HSP105（STRING 967）——HSP105是HSP70的核苷酸交换因子（NEF），与DNAJB4协同促进HSP70的底物结合-释放循环。若DNAJB4-HSPA1A/B形成功能性伴侣模块，则可能直接参与L1 ORF2p（逆转录酶）新生链的折叠——与HSPA14的RAC复合物构成从合成到折叠的完整监督路径。

**DNAJB4-HSPA14共调控的协同TE抑制假说**：DNAJB4（HSP40伴侣）与HSPA14（RAC复合物HSP70组分, 第8号候选）共享PPI伙伴（DNAJC2 STRING 865, HSPA12B STRING 803）的潜在共调控网络。若DNAJB4将未折叠的L1 ORF1p/ORF2p新生链"递送"给RAC复合物，HSPA14可能接着执行折叠或泛素化导向的降解——形成协同的TE蛋白质量控制路径。AlphaFold pLDDT=82.7和PDB=0的结构缺失需实验结构补足。CRISPR敲除DNAJB4后通过ribosome profiling检测L1 ORF1p/ORF2p的翻译效率变化是验证协同假说的首选实验。


### 补充分析 (UniProt API)

**蛋白全称**: DnaJ homolog subfamily B member 4

**功能**: Probable chaperone. Stimulates ATP hydrolysis and the folding of unfolded proteins mediated by HSPA1A/B (in vitro) (PubMed:24318877)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR002939 |
| InterPro | IPR001623 |
| InterPro | IPR018253 |
| InterPro | IPR051339 |
| InterPro | IPR008971 |
| InterPro | IPR036869 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| HSPA4 | STRING | 982 |
| HSPA1B | STRING | 976 |
| HSPA8 | STRING | 967 |
| HSPH1 | STRING | 967 |
| HSPA6 | STRING | 947 |
| HSPA1A | STRING | 941 |
| HSPA1L | STRING | 938 |
| DNAJC2 | STRING | 865 |