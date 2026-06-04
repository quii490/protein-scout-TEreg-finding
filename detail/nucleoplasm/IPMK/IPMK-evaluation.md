---
type: protein-evaluation
gene: "IPMK"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## IPMK 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | IPMK / IPMK|IMPK|PI(3)K|IP3K|IPK2 |
| 蛋白全称 | Inositol polyphosphate multikinase |
| 蛋白大小 | 416 aa / ~45.8 kDa |
| UniProt ID |  |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/IPMK/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/IPMK/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | x4 | 32 | 核定位：UniProt Nucleus + 微量胞质背景 |
| 蛋白大小 | 10/10 | x1 | 10 | 416 aa，适宜 |
| 研究新颖性 | 2/10 | x5 | 30 | PubMed 83 篇 |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold pLDDT≥80，高质量预测 |
| 调控结构域 | 7/10 | x2 | 14 | 新颖蛋白基线 (7/10) |
| PPI 网络 | 2/10 | x3 | 6 | 互作数据有限 (2/10) |
| 互证加分 | +1 | max +3 | +1 | — |
|  | **原始总分** |  | **97/183** | **96.0/183** |  |  |  |
|  | **归一化总分** |  | **53.0/100** | **52.5/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Nucleus | — |
| Protein Atlas (IF) | 暂无数据（HPA IF 图像已本地嵌入。

| UniProt | Nucleus | — |
| GO Cellular Component | ciliary basal body | cytoplasm | nucleoplasm | nucleus | — |

**结论**: 核定位：UniProt Nucleus + 微量胞质背景。UniProt 明确标注 Nucleus 定位。HPA 暂无 IF 数据，核定位判断主要基于 UniProt + GO。

#### 3.2 蛋白大小评估

**评价**: 416 aa (~45.8 kDa)，适合常规生化实验和结构解析，大小接近理想范围（200–800 aa）。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 83 |
| 新颖性评级 | 有一定研究但 niche 空间充足 |

**主要研究方向**:
- Inositol polyphosphate multikinase 的功能研究
- 转录调控/信号传导相关

**评价**: PubMed 83 篇，有一定研究基础，但 niche 空间充足。

**关键文献**:
1. Zou X et al. (2024). "Hypoxia-inducible factor 2α promotes pathogenic polarization of stem-like Th2 cells via modulation of phospholipid metabolism". *Immunity*. PMID: 39609127
2. Jung IR et al. (2023). "Time-restricted feeding ameliorates MCDD-induced steatohepatitis in mice". *bioRxiv*. PMID: 38014152
3. Lee H et al. (2023). "miRNA-Induced Downregulation of IPMK in Macrophages Mediates Lipopolysaccharide-Triggered TLR4 Signaling". *Biomolecules*. PMID: 36830701
4. Sin Z et al. (2025). "IPMK depletion influences genome-wide DNA methylation". *Biochem Biophys Res Commun*. PMID: 40300331
5. Malabanan MM & Blind RD (2016). "Inositol polyphosphate multikinase (IPMK) in transcriptional regulation and nuclear inositide metabolism". *Biochem Soc Trans*. PMID: 26862216
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 全局 pLDDT | 73.75 |
| pLDDT > 90 占比 | 54% |
| pLDDT > 70 占比 | 60% |
| AlphaFold 版本 | v6 |
| 可用 PDB 条目 | 25 个：5W2G, 5W2H, 5W2I, 6E7F, 6M88, 6M89, 6M8A, 6M8B |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/IPMK/IPMK-PAE.png]]

**评价**: AlphaFold pLDDT≥80，高质量预测。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt InterPro | IPK, IPK_sf |
| Pfam | IPK |

**染色质调控潜力分析**: 未注释到经典染色质/DNA 结合结构域，但属于新颖蛋白（基线不扣分）。AlphaFold 预测有可辨识折叠域，存在新结构域发现潜力。

#### 3.6 PPI 网络

**实验验证互作** (IntAct):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |

**STRING 预测互作** (combined score >0.4):
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| IPPK | 0.000 | — | — |
| ITPK1 | 0.045 | — | — |
| MINPP1 | 0.053 | — | — |
| ITPKB | 0.000 | — | — |
| ITPKA | 0.000 | — | — |


**已知复合体成员** (GO Cellular Component):
- ciliary basal body

**PPI 互证分析**:
- 物理互作证据：IntAct 有实验互作数据
- STRING 预测：30 个 partner，>0.7 高置信度较少
- 调控相关比例：需进一步验证

**评价**: 互作数据有限 (2/10)。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT + PDB | pLDDT=73.75, PDB=25个 | — |
| 结构域 | InterPro / Pfam / SMART | IPK, IPK_sf | — |
| PPI | STRING + IntAct | 有网络 | — |
| 定位 | UniProt / GO | Nucleus | — |

**互证加分明细**: STRONG + UniProt/GO 一致，+1。

### 4. 总体评价

**推荐等级**: ★★★☆☆ (63.9/100)

**核心优势**:
1. 研究新颖（PubMed 83 篇）
2. 核定位：UniProt Nucleus + 微量胞质背景
3. AlphaFold pLDDT≥80，高质量预测

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
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=IPMK
- STRING: https://string-db.org/network/9606.ENSP00000000
- IntAct: https://www.ebi.ac.uk/intact/search?query=IPMK


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[IPMK-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/IPMK/IPMK-PAE.png]]


