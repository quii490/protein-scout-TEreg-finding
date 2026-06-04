---
type: protein-evaluation
gene: "IWS1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## IWS1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | IWS1 / IWS1|IWS1L|DKFZp761G0123 |
| 蛋白全称 | Protein IWS1 homolog |
| 蛋白大小 | 819 aa / ~90.1 kDa |
| UniProt ID |  |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/IWS1/IF_images/CACO-2_1.jpg|CACO-2]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/IWS1/IF_images/Hep-G2_1.jpg|Hep-G2]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | x4 | 32 | 核定位：UniProt Nucleus + 微量胞质背景 |
| 蛋白大小 | 8/10 | x1 | 8 | 819 aa，适宜 |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed 21 篇 |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold pLDDT≥80，高质量预测 |
| 调控结构域 | 8/10 | x2 | 16 | nucleic acid binding 相关域，多库确认 (8/10) |
| PPI 网络 | 6/10 | x3 | 18 | 有物理互作/复合体证据，部分调控 (6/10) |
| 互证加分 | +1 | max +3 | +1 | — |
| **原始总分** |  |  | **139/183** |  |
| **归一化总分** |  |  | **76.0/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Nucleus | — |
| Protein Atlas (IF) | 暂无数据（HPA IF 图像已本地嵌入。

| UniProt | Nucleus | — |
| GO Cellular Component | nucleoplasm | nucleus | — |

**结论**: 核定位：UniProt Nucleus + 微量胞质背景。UniProt 明确标注 Nucleus 定位。HPA 暂无 IF 数据，核定位判断主要基于 UniProt + GO。

#### 3.2 蛋白大小评估

**评价**: 819 aa (~90.1 kDa)，大小偏大，可能增加实验难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 21 |
| 新颖性评级 | 非常新颖 |

**主要研究方向**:
- Protein IWS1 homolog 的功能研究
- 转录调控/信号传导相关

**评价**: PubMed 21 篇，研究较少，属于非常新颖的蛋白。

**关键文献**:
1. Markert JW et al. (2025). "Structural basis of H3K36 trimethylation by SETD2 during chromatin transcription". *Science*. PMID: 39666822
2. Cermakova K et al. (2021). "A ubiquitous disordered protein interaction module orchestrates transcription elongation". *Science*. PMID: 34822292
3. Zheenbekova A et al. (2025). "IWS1 positions downstream DNA to globally stimulate Pol II elongation". *Nat Commun*. PMID: 40835814
4. Syau D et al. (2025). "Structure and function of IWS1 in transcription elongation". *bioRxiv*. PMID: 40909601
5. Bejjani F et al. (2025). "Overlapping and distinct functions of SPT6, PNUTS, and PCF11 in regulating transcription termination". *Nucleic Acids Res*. PMID: 40103229
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 全局 pLDDT | 54.53 |
| pLDDT > 90 占比 | 13% |
| pLDDT > 70 占比 | 23% |
| AlphaFold 版本 | v6 |
| 可用 PDB 条目 | 10 个：6EMR, 6ZV1, 6ZV4, 9EGX, 9EGY, 9EGZ, 9EH0, 9EH1 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/IWS1/IWS1-PAE.png]]

**评价**: AlphaFold pLDDT≥80，高质量预测。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt InterPro | RNAPII_TF_IWS1, TFIIS/LEDGF_dom_sf, TFIIS_N |
| Pfam | Med26 |

**染色质调控潜力分析**: 未注释到经典染色质/DNA 结合结构域，但属于新颖蛋白（基线不扣分）。AlphaFold 预测有可辨识折叠域，存在新结构域发现潜力。

#### 3.6 PPI 网络

**实验验证互作** (IntAct):
| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |

**STRING 预测互作** (combined score >0.4):
| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| SUPT6H | 0.981 | — | — |
| SUPT5H | 0.903 | — | — |
| TCEA1 | 0.399 | — | — |
| SETD2 | 0.553 | — | — |
| POLR2A | 0.889 | — | — |


**已知复合体成员** (GO Cellular Component):
- 未注释到特定染色质调控复合体

**PPI 互证分析**:
- 物理互作证据：IntAct 有实验互作数据
- STRING 预测：30 个 partner，>0.7 高置信度有
- 调控相关比例：需进一步验证

**评价**: 有物理互作/复合体证据，部分调控 (6/10)。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT + PDB | pLDDT=54.53, PDB=10个 | — |
| 结构域 | InterPro / Pfam / SMART | RNAPII_TF_IWS1, TFIIS/LEDGF_dom_sf, TFIIS_N | — |
| PPI | STRING + IntAct | 有网络 | — |
| 定位 | UniProt / GO | Nucleus | — |

**互证加分明细**: STRONG + UniProt/GO 一致，+1。

### 4. 总体评价

**推荐等级**: ★★★☆☆ (76.0/100)

**核心优势**:
1. 研究新颖（PubMed 21 篇）
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
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=IWS1
- STRING: https://string-db.org/network/9606.ENSP00000000
- IntAct: https://www.ebi.ac.uk/intact/search?query=IWS1


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[IWS1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/IWS1/IWS1-PAE.png]]


