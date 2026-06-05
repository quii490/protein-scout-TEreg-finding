---
type: protein-evaluation
gene: "PPM1F"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PPM1F 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PPM1F / FEM-2|KIAA0015|POPX2|CaMKPase|CAMKP |
| 蛋白全称 | Protein phosphatase 1F |
| 蛋白大小 | 454 aa |
| UniProt ID | P49593 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | **16** | Nuclear + cyto, no preference |
| 蛋白大小 | 10/10 | ×1 | **10** | 454 aa，处于理想范围 |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed 64 篇，中等研究热度 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 9 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+0.5** | 多库结构域一致 (+0.5) |
|  | **原始总分** |  | **84.5/183** | **84.0/183** |  |  |  |
|  | **归一化总分** |  | **46.2/100** | **45.9/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt |  | 实验证据/预测 |
| GO-CC | GO:0005634 | IBA|IEA|ISS |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PPM1F/IF_images/A-431_HPA030989_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PPM1F/IF_images/U-251MG_HPA030989_2.jpg|U-251MG]]

**结论**: Nuclear + cyto, no preference

#### 3.2 蛋白大小评估

**评价**: 454 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 64 |

**评价**: PubMed 64 篇，中等研究热度

**关键文献**:
1. Kamada R et al. (2020). "Metal-dependent Ser/Thr protein phosphatase PPM family: Evolution, structures, diseases and inhibitors". *Pharmacol Ther*. PMID: 32650009
2. Tu SH et al. (2016). "Protein phosphatase Mg2+/Mn2+ dependent 1F promotes smoking-induced breast cancer by inactivating phosphorylated-p53-induced signals". *Oncotarget*. PMID: 27769050
3. Liu J et al. (2023). "Medial prefrontal cortical PPM1F alters depression-related behaviors by modifying p300 activity via the AMPK signaling pathway". *CNS Neurosci Ther*. PMID: 37309288
4. Liao Y et al. (2021). "CircSEC24A promotes tumor progression through sequestering miR-455-3p in hepatocellular carcinoma". *Neoplasma*. PMID: 34459207
5. Grimm TM et al. (2022). "Lockdown, a selective small-molecule inhibitor of the integrin phosphatase PPM1F, blocks cancer cell invasion". *Cell Chem Biol*. PMID: 35443151
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 454 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 9 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PPM1F/PPM1F-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | PP2C |
| InterPro | PP2C_BS |
| InterPro | PPM-type-like_dom_sf |
| InterPro | PPM-type_phosphatase-like_dom |
| Pfam | PP2C |
| SMART | PP2C_SIG |
| SMART | PP2Cc |
| PROSITE | PPM_1 |
| PROSITE | PPM_2 |

**染色质调控潜力分析**: 9 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:protein-containing complex (GO:0032991, IDA:UniProtKB)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 9 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | Partially consistent |

**互证加分明细**:
多库结构域一致 (+0.5)
**总计**: +0.5

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 64 篇，中等研究热度
2. 核定位: needs confirmation

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=PPM1F
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100034-PPM1F
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22PPM1F%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/P49593
- STRING: https://string-db.org/network/9606.ENSG00000100034
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P49593


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[PPM1F-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PPM1F/PPM1F-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000100034-PPM1F/subcellular

![](https://images.proteinatlas.org/30989/1246_E1_2_red_green.jpg)
![](https://images.proteinatlas.org/30989/1246_E1_3_red_green.jpg)
![](https://images.proteinatlas.org/30989/381_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/30989/381_E5_3_red_green.jpg)
![](https://images.proteinatlas.org/30989/398_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/30989/398_E5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
