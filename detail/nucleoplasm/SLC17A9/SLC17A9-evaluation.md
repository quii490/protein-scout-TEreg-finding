---
type: protein-evaluation
gene: "SLC17A9"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SLC17A9 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SLC17A9 |
| 蛋白名称 | Voltage-gated purine nucleotide uniporter SLC17A9 |
| 蛋白大小 | 436 aa / 47.5 kDa |
| UniProt ID | Q9BYT1 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 436 aa |
| 新颖性 | 8/10 | x5 | 40.0 | PubMed=45 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=89.5; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | MFS; MFS_dom; MFS_Na/Anion_cotransporter |
| PPI | 5/10 | x3 | 15.0 | PPI degree=7 |
| **加权总分** | | | **129/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=45 broad=108
- AF pLDDT=89.5 PDB=0
- InterPro: MFS; MFS_dom; MFS_Na/Anion_cotransporter
- Pfam: MFS_1
- PPI degree=7 ChIP: None
36440584: NLRP3 Inflammasome Activation Through Heart-Brain Interaction Initiates Cardiac  | 40302348: Co-Highly Expressed SLC17A9 and KCNH1 as Potential Prognostic Biomarkers and The | 36590170: SLC17A9-PTHLH-EMT axis promotes proliferation and invasion of clear renal cell c

### 4. 总体评价
**71.6/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

SLC17A9是主要协同转运蛋白超家族（MFS）的成员，通过12次跨膜α-螺旋形成典型的MFS折叠通道（IPR011701/MFS_dom），利用膜电位作为驱动力介导ATP向溶酶体和分泌囊泡内的单向转运——被称为囊泡核苷酸转运体（VNUT）。AlphaFold预测pLDDT高达89.5（无PDB结构），反映了MFS折叠的高度保守性及预测置信度。436个氨基酸的紧凑拓扑结构以中央底物结合腔为核心，通过摇杆开关（rocker-switch）机制在胞质开放与腔体（溶酶体/囊泡腔）开放构象之间交替，实现嘌呤核苷酸的跨膜易位。

HPA Approved的Nucleoplasm定位与该蛋白经典的内体/溶酶体膜定位形成鲜明对比，暗示了一种非经典核定位机制。SLC17A9可能嵌入内核膜（INM）或核孔周围的核膜微域，介导核内ATP稳态的微调——核内ATP是染色质重塑、RNA加工和DNA修复等耗能过程的必需底物。PPI网络（degree=7）虽小但引人注目，其中RPA2（复制蛋白A）的互作强烈指向DNA复制/修复功能——RPA是ssDNA结合蛋白，其活性依赖ATP依赖性构象变化。

SLC17A9的核功能假说得到疾病关联数据的间接支持：SLC17A9-PTHLH-EMT轴促进肾透明细胞癌的增殖与侵袭（PMID:36590170），而NLRP3炎症小体激活涉及该蛋白的心脏-脑互作信号（PMID:36440584）。这些观察暗示SLC17A9介导的ATP释放在肿瘤微环境和神经炎症中均发挥关键病理生理角色。核内SLC17A9池可能通过调节局部ATP浓度影响PARP家族酶活性、SWI/SNF染色质重塑复合体功能或RNA解旋酶的核内活性。

从TE调控角度看，SLC17A9作为已获HPA Approved核定位且结构预测质量极高（pLDDT=89.5）的膜转运蛋白，其核功能的发现将为"核代谢"（nuclear metabolism）这一新兴领域提供有力的分子机制支持。PubMed文献108篇主要聚焦于神经递质释放和炎症小体激活，核内功能的系统性研究几乎空白——这为新发现留下了巨大的探索空间。鉴于其与核蛋白RPA2、SCAND1（含SCAN锌指转录因子）及SMG9（无义介导的mRNA降解因子）的互作，SLC17A9的核内功能可能涉及基因组稳定性与mRNA质量控制。

**蛋白全称**: Voltage-gated purine nucleotide uniporter SLC17A9

**功能**: Voltage-gated ATP nucleotide uniporter that can also transport the purine nucleotides ADP and GTP. Uses the membrane potential as the driving force to control ATP accumulation in lysosomes and secretory vesicles (PubMed:18375752, PubMed:23467297). By controlling ATP storage in lysosomes, regulates ATP-dependent proteins of these organelles (PubMed:35269509). Also indirectly regulates the exocytosis of ATP through its import into lysosomes in astrocytes and secretory vesicles such as adrenal chro

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR011701 |
| InterPro | IPR020846 |
| InterPro | IPR050382 |
| InterPro | IPR036259 |
| InterPro | IPR044777 |
| InterPro | IPR005829 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| RPA2 | BioGRID | 1 |
| C12ORF10 | BioGRID | 1 |
| SCAND1 | BioGRID | 1 |
| SMG9 | BioGRID | 0 |
| C12orf10 | BioGRID | 0 |
| TARS2 | BioGRID | 0 |
| MTERF3 | BioGRID | 0 |
| DIABLO | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9BYT1-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000101194-SLC17A9

![](https://images.proteinatlas.org/47470/1027_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/47470/1027_F10_4_red_green.jpg)
![](https://images.proteinatlas.org/47470/763_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/47470/763_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/47470/737_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/47470/737_F2_2_red_green.jpg)

### PubMed 文献

**PubMed count: 108**

| 41896365 | ATP release from the amygdala-prefrontal pathway regulates vulnerability to social stress in male mice. | Mol Psychiatry 2026 |
| 41643455 | Vesicular nucleotide transporter (VNUT)-dependent ATP secretion by hepatic stellate cells promotes liver fibrosis. | Biochim Biophys Acta Mol Basis Dis 2026 |
| 41553569 | A ceRNA Network Mediates Salinity Adaptation Via miR-novel-3-LNC_015168-SLC17A9 Axis in Sea Cucumber. | Mar Biotechnol (NY) 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SLC17A9

