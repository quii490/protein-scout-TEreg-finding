---
type: protein-evaluation
gene: "AKAP6"
date: 2026-06-03
tags: [protein-scout, rejected]
status: rejected
rejection_reason: nuclear_score ≤ 3
---

## AKAP6 核蛋白评估报告（重新评估）

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AKAP6 / AKAP100 / KIAA0311 |
| 蛋白大小 | 2319 aa / 256.7 kDa |
| UniProt ID | Q13023 |
| 蛋白全名 | A-kinase anchor protein 6 |
| HPA IF 主定位 | (无数据) |
| HPA Reliability | (无) |
| 评估日期 | 2026-06-03 |
| 评估结果 | **REJECTED** (nuclear_score=3) |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA无数据；UniProt注释Nuclear membrane/Sarcoplasmic reticulum |
| 蛋白大小 | 4/10 | ×1 | 4 | 2319aa/256.7kDa，极大蛋白，实验困难 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=30 (21-40→8) |
| 三维结构 | 2/10 | ×3 | 6 | pLDDT=42.1, pct<50=73.6%，几乎全无序 |
| 调控结构域 | 6/10 | ×2 | 12 | IPR018159 (AKAP anchoring)，PKA锚定调控 |
| PPI网络 | 7/10 | ×3 | 21 | RYR2(0.992), PRKACA(0.953), PDE4D(0.944); 强信号通路PPI |
| **加权总分** | | | **95/180** | |
| **归一化总分 (÷1.8)** | | | **52.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | 无 IF 数据 (no_image_detected) | N/A |
| UniProt | Sarcoplasmic reticulum, Nucleus membrane | |
| GO-CC | GO:0005635 (nuclear envelope, IDA), GO:0031965 (nuclear membrane, IEA), GO:0014704 (intercalated disc), GO:0016529 (sarcoplasmic reticulum) | |

HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。HPA 无 IF 图像数据。UniProt 注释核膜和肌质网，GO-CC 含 nuclear envelope (IDA)。蛋白主要定位在心肌细胞的肌质网/核膜界面。**评分: 3/10**。

#### 3.2 蛋白大小评估

2319 aa / 256.7 kDa。极大蛋白，远超实验操作理想范围。重组全长几乎不可能，需截短体策略。**评分: 4/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 30 |
| PubMed symbol_only | 46 |
| 别名 | AKAP100, KIAA0311 |
| 主要方向 | 心肌钙信号、RyR2调控、PKA锚定 |

**评价**: PubMed 30 篇 (strict)，中等新颖度。AKAP6 是 PKA 锚定蛋白家族成员，功能高度集中在心肌钙信号和 RyR2 磷酸化调控。**评分: 8/10** (21-40篇)。

**关键文献**:
1. Tomczak J et al. (2024). "Exploring AKAPs in visual signaling." *Front Mol Neurosci*. PMID: 38813437
2. Hakem Zadeh F et al. (2019). "AKAP6 and phospholamban colocalize and interact in HEK-293T cells and primary murine cardiomyocytes." *Physiol Rep*. PMID: 31325238
3. Lee SW et al. (2015). "AKAP6 inhibition impairs myoblast differentiation and muscle regeneration." *Sci Rep*. PMID: 26563778
4. Zhang M et al. (2019). "Impact of AKAP6 polymorphisms on Glioma susceptibility and prognosis." *BMC Neurol*. PMID: 31759389
5. Li A et al. (2025). "Wnt/β-catenin pathway induces cardiac dysfunction via AKAP6-mediated RyR2 phosphorylation." *J Mol Cell Biol*. PMID: 40097291

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 42.1 |
| pLDDT > 90 (Very High) | 1.9% |
| pLDDT 70-90 (High) | 17.1% |
| pLDDT 50-70 (Medium) | 7.4% |
| pLDDT < 50 (Low) | 73.6% |
| 有序区域 (pLDDT>70) | 19.0% |
| 实验结构 (PDB) | 无 |

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。AlphaFold 预测质量极低 (pLDDT 42.1)，73.6% 残基 pLDDT < 50，提示蛋白几乎全为无序区域。作为大型支架蛋白，IDR 占比高符合预期。**评分: 2/10**。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR018159 (Spectrin/alpha-actinin); IPR002017 (Spectrin repeat) |
| Pfam | PF00435 (Spectrin repeat) |

AKAP6 含多个血影蛋白重复序列 (Spectrin repeats)，介导 PKA 的亚细胞锚定。功能为将 PKA II 型调节亚基靶向至核膜或肌质网。作为信号支架蛋白具有调控功能，但血影蛋白重复本身不直接参与转录或染色质调控。**评分: 6/10**。

#### 3.6 PPI 网络

**STRING 预测互作** (top 10):

| Partner | Score | 实验证据 | 功能类别 |
|---------|-------|---------|---------|
| RYR2 | 0.992 | 0.496 | 心肌钙释放通道 |
| RAPGEF3 | 0.967 | 0.095 | cAMP信号 |
| MAPK7 | 0.958 | 0 | MAPK信号 |
| PRKACB | 0.953 | 0.091 | PKA催化亚基 |
| PRKACA | 0.953 | 0.091 | PKA催化亚基 |
| PDE4D | 0.944 | 0.292 | cAMP磷酸二酯酶 |
| PDE4A | 0.941 | 0.292 | cAMP磷酸二酯酶 |
| AKAP1 | 0.931 | 0 | 线粒体AKAP |
| FKBP1B | 0.929 | 0 | RyR2调控 |
| AKAP7 | 0.809 | 0 | 同家族AKAP |

**PPI 互证分析**: PPI 网络高度集中在 cAMP/PKA 信号和钙调控通路。RYR2 为最核心互作伙伴，有实验证据。IntAct 确认 RYR2/PRKACA 互作。信号通路清晰但局限于肌细胞生理学。**评分: 7/10**。

### 4. 拒绝理由

AKAP6 nuclear_score=3 (≤3 阈值)，核心原因：
- HPA 无可用的 IF 图像数据
- AlphaFold 几乎全无序 (pLDDT 42.1)
- 蛋白极大 (2319 aa)，实验操作困难
- 功能高度专一于心肌钙信号，核关联弱

**结论**: 即使在信号通路研究中重要，AKAP6 的核定位证据不足、结构无序化严重、大小不适合常规生化实验，不符合核蛋白筛选标准。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13023
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13023
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AKAP6%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/ENSG00000151320-AKAP6
