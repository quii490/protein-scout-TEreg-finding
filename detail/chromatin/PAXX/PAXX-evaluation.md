---
type: protein-evaluation
gene: "PAXX"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PAXX 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PAXX / XLS |
| 蛋白全称 | Protein PAXX |
| 蛋白大小 | 204 aa |
| UniProt ID | Q9BUH6 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/PAXX/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/PAXX/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | **28** | UniProt 核定位，部分细胞质 |
| 蛋白大小 | 10/10 | ×1 | **10** | 204 aa，处于理想范围 |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed 66 篇，中等研究热度 |
| 三维结构 | 10/10 | ×3 | **30** | 17 个 PDB 结构 |
| 调控结构域 | 7/10 | ×2 | **14** | 3 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+1.5** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5) |
|  | **原始总分** |  | **109/183** | **108.0/183** |  |  |
|  | **归一化总分** |  | **59.6/100** | **59.0/100** |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus, Chromosome, Cytoplasm | 实验证据/预测 |
| GO-CC | GO:0005634 | IBA|IDA|IEA|IMP |

**结论**: UniProt Nucleus + partial cyto

#### 3.2 蛋白大小评估

**评价**: 204 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 66 |

**关键文献**:
1. Liu et al. (2025). "Dynamic assemblies and coordinated reactions of non-homologous end joining.". *Nature*. PMID: 40500445
2. de et al. (2025). "A comprehensive genetic catalog of human double-strand break repair.". *Science*. PMID: 41037600
3. Seif-El-Dahan et al. (2023). "PAXX binding to the NHEJ machinery explains functional redundancy with XLF.". *Sci Adv*. PMID: 37256950
4. Lu et al. (2025). "SPHK1-S1p Signaling Drives Fibrocyte-Mediated Pulmonary Fibrosis: Mechanistic Insights and Therapeutic Potential.". *Pharmaceuticals (Basel)*. PMID: 40573254
5. Gluza et al. (2025). "PAXX/Ku interaction is rate limiting for repair of double-strand DNA breaks requiring end processing.". *J Biol Chem*. PMID: 40659092
**评价**: PubMed 66 篇，中等研究热度

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 204 aa |
| PDB 条数 | 17 |
| 已注释结构域 | 3 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/chromatin/PAXX/PAXX-PAE.png]]

**评价**: 17 个 PDB 结构

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | PAXX |
| InterPro | PAXX_N |
| Pfam | PAXX |

**染色质调控潜力分析**: 3 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:nonhomologous end joining complex (GO:0070419, IDA:UniProtKB)


**PPI 互证分析**:
- （待补充：综合 STRING、IntAct 和 GO 数据库的互作信息，分析 PPI 网络的一致性）
**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 17 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 3 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
PDB + AlphaFold 结构互证 (+0.5)
**总计**: +1.5

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 66 篇，中等研究热度
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 17 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=PAXX
- Protein Atlas: https://www.proteinatlas.org/ENSG00000148362-PAXX
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22PAXX%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9BUH6
- STRING: https://string-db.org/network/9606.ENSG00000148362
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BUH6


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[PAXX-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/PAXX/PAXX-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000148362-PAXX/subcellular

![](https://images.proteinatlas.org/45268/526_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/45268/526_E1_2_red_green.jpg)
![](https://images.proteinatlas.org/45268/528_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/45268/528_E1_2_red_green.jpg)
![](https://images.proteinatlas.org/45268/545_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/45268/545_E1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
