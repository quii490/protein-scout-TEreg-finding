---
type: protein-evaluation
gene: "OTUD5"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## OTUD5 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | OTUD5 / DKFZp761A052|DUBA |
| 蛋白全称 | OTU domain-containing protein 5 |
| 蛋白大小 | 571 aa |
| UniProt ID | Q96G74 |
| 评估日期 | 2026-05-30 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/OTUD5/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/OTUD5/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 10/10 | ×1 | **10** | 571 aa，处于理想范围 |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed 79 篇，中等研究热度 |
| 三维结构 | 8/10 | ×3 | **24** | 3 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 5 个已注释结构域 |
| PPI 网络 | 4/10 | ×3 | **12** | STRING 15 个互作伙伴，调控相关性低 |
| 互证加分 | -- | -- | **+2.0** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5); 多库结构域一致 (+0.5) |
|  | **原始总分** |  | **113/183** | **112.0/183** |  |  |
|  | **归一化总分** |  | **61.7/100** | **61.2/100** |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| HPA IF | 暂无数据（待细胞分析），核定位基于 UniProt + GO 注释 | -- |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | N/A | N/A |

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 571 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 79 |

**关键文献**:
1. Zhao et al. (2024). "Podocyte OTUD5 alleviates diabetic kidney disease through deubiquitinating TAK1 and reducing podocyte inflammation and injury.". *Nat Commun*. PMID: 38937512
2. Liu et al. (2023). "Deubiquitinase OTUD5 as a Novel Protector against 4-HNE-Triggered Ferroptosis in Myocardial Ischemia/Reperfusion Injury.". *Adv Sci (Weinh)*. PMID: 37552043
3. Chu et al. (2023). "Autophagy of OTUD5 destabilizes GPX4 to confer ferroptosis-dependent kidney injury.". *Nat Commun*. PMID: 38110369
4. Morita et al. (2025). "Combinatorial ubiquitin code degrades deubiquitylation-protected substrates.". *Nat Commun*. PMID: 40128189
5. Liu et al. (2025). "THBS1 in macrophage-derived exosomes exacerbates cerebral ischemia-reperfusion injury by inducing ferroptosis in endothelial cells.". *J Neuroinflammation*. PMID: 39994679
**评价**: PubMed 79 篇，中等研究热度

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 571 aa |
| PDB 条数 | 3 |
| 已注释结构域 | 5 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/OTUD5/OTUD5-PAE.png]]

**评价**: 3 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | OTU_dom |
| InterPro | Papain-like_cys_pep_sf |
| InterPro | Peptidase_C85-like |
| Pfam | OTU |
| PROSITE | OTU |

**染色质调控潜力分析**: 5 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|
| TRAF3 | 0 |  | no |
| UBC | 0 |  | no |
| RPS27A | 0 |  | no |
| UBB | 0 |  | no |
| UBA52 | 0 |  | no |
| TBK1 | 0 |  | no |
| UBR5 | 0 |  | no |
| ZUP1 | 0 |  | no |
| IKBKE | 0 |  | no |
| OTUB1 | 0 |  | no |

**已知复合体成员** (GO-CC):

--


**PPI 互证分析**:
- （待补充：综合 STRING、IntAct 和 GO 数据库的互作信息，分析 PPI 网络的一致性）
**评价**: STRING 15 个互作伙伴，调控相关性低

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 3 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 5 个 | 多库一致 |
| PPI 网络 | STRING | 15 个 | 单一来源 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
PDB + AlphaFold 结构互证 (+0.5)
多库结构域一致 (+0.5)
**总计**: +2.0

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 79 篇，中等研究热度
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 3 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=OTUD5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000068308-OTUD5
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22OTUD5%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q96G74
- STRING: https://string-db.org/network/9606.ENSG00000068308
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96G74


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[OTUD5-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/OTUD5/OTUD5-PAE.png]]




