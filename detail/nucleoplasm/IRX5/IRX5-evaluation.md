---
type: protein-evaluation
gene: "IRX5"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## IRX5 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | IRX5 / IRX5|IRX2A|IRXB2 |
| 蛋白全称 | Iroquois-class homeodomain protein IRX-5 |
| 蛋白大小 | 483 aa / ~53.1 kDa |
| UniProt ID |  |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/IRX5/IF_images/HaCaT_1.jpg|HaCaT]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/IRX5/IF_images/MCF-7_1.jpg|MCF-7]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | x4 | 36 | 严格核蛋白：UniProt Nucleus + GO 支持（HPA 无 IF 数据） |
| 蛋白大小 | 10/10 | x1 | 10 | 483 aa，适宜 |
| 研究新颖性 | 4/10 | x5 | 30 | PubMed 69 篇 |
| 三维结构 | 6/10 | x3 | 18 | 新颖蛋白基线 (6/10) |
| 调控结构域 | 10/10 | x2 | 20 | 明确 chromatin/DNA-binding 结构域 |
| PPI 网络 | 2/10 | x3 | 6 | 互作数据有限 (2/10) |
| 互证加分 | +0 | max +3 | +0 | — |
|  | **原始总分** |  | **110/183** | **110.0/183** |  |  |  |
|  | **归一化总分** |  | **60.1/100** | **60.1/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Nucleus | — |
| Protein Atlas (IF) | IF image available (embedded above) | See IF_images/ |
| UniProt | Nucleus | — |
| GO Cellular Component | chromatin | nucleus | — |

**结论**: 严格核蛋白：UniProt Nucleus + GO 支持（HPA 无 IF 数据）。UniProt 明确标注 Nucleus 定位。HPA 暂无 IF 数据，核定位判断主要基于 UniProt + GO。

#### 3.2 蛋白大小评估

**评价**: 483 aa (~53.1 kDa)，适合常规生化实验和结构解析，大小接近理想范围（200–800 aa）。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 69 |
| 新颖性评级 | 有一定研究但 niche 空间充足 |

**主要研究方向**:
- Iroquois-class homeodomain protein IRX-5 的功能研究
- 转录调控/信号传导相关

**评价**: PubMed 69 篇，有一定研究基础，但 niche 空间充足。

**关键文献**:
1. Littleton SH et al. (2020). "Genetic Determinants of Childhood Obesity". *Mol Diagn Ther*. PMID: 33006084
2. Claussnitzer M et al. (2015). "FTO Obesity Variant Circuitry and Adipocyte Browning in Humans". *N Engl J Med*. PMID: 26287746
3. Chen JK et al. (2023). "IRX5 promotes DNA damage repair and activation of hair follicle stem cells". *Stem Cell Reports*. PMID: 37084727
4. Steinwand S et al. (2025). "Conserved noncoding cis elements associated with hibernation modulate metabolic and behavioral adaptations in mice". *Science*. PMID: 40743330
5. Jiang B et al. (2024). "IRX5 suppresses osteogenic differentiation of hBMSCs by inhibiting protein synthesis". *J Cell Physiol*. PMID: 38666481
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 全局 pLDDT | 54.31 |
| pLDDT > 90 占比 | 10% |
| pLDDT > 70 占比 | 12% |
| AlphaFold 版本 | v6 |
| 可用 PDB 条目 | 0 个 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/IRX5/IRX5-PAE.png]]

**评价**: 新颖蛋白基线 (6/10)。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt InterPro | HD, Homeobox_CS, Homeodomain-like_sf, Iroquois_homeo, KN_HD |
| Pfam | Homeobox_KN |

**染色质调控潜力分析**: 包含明确的 DNA 结合/染色质调控结构域：Homeobox_CS, Homeodomain-like_sf

#### 3.6 PPI 网络

**实验验证互作** (IntAct):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |

**STRING 预测互作** (combined score >0.4):
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| IRX3 | 0.000 | — | — |
| KCND2 | 0.000 | — | — |
| SMYD1 | 0.056 | — | — |
| HAND2 | 0.047 | — | — |
| KCNE4 | 0.000 | — | — |


**已知复合体成员** (GO Cellular Component):
- chromatin

**PPI 互证分析**:
- 物理互作证据：IntAct 有实验互作数据
- STRING 预测：29 个 partner，>0.7 高置信度较少
- 调控相关比例：需进一步验证

**评价**: 互作数据有限 (2/10)。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT + PDB | pLDDT=54.31, PDB=0个 | — |
| 结构域 | InterPro / Pfam / SMART | HD, Homeobox_CS, Homeodomain-like_sf, Iroquois_homeo, KN_HD | — |
| PPI | STRING + IntAct | 有网络 | — |
| 定位 | UniProt / GO | Nucleus | — |

**互证加分明细**: 无额外互证加分。

### 4. 总体评价

**推荐等级**: ★★★☆☆ (65.6/100)

**核心优势**:
1. 研究新颖（PubMed 69 篇）
2. 严格核蛋白：UniProt Nucleus + GO 支持（HPA 无 IF 数据）
3. 新颖蛋白基线 (6/10)

**风险/不确定性**:
1. HPA IF 数据缺失，核定位待实验验证
2. PPI 数据有限，调控网络待探索
3. 功能研究较少，生物学角色待阐明

**下一步建议**:
- [ ] 获取 HPA IF 数据或多重 IF 验证核定位
- [ ] Co-IP/MS 鉴定互作伙伴
- [ ] ChIP-seq 分析基因组结合位点（如为 TF/染色质蛋白）

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/
- AlphaFold: https://alphafold.ebi.ac.uk/entry/
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=IRX5
- STRING: https://string-db.org/network/9606.ENSP00000000
- IntAct: https://www.ebi.ac.uk/intact/search?query=IRX5


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[IRX5-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/IRX5/IRX5-PAE.png]]




