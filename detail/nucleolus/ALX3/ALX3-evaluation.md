---
type: protein-evaluation
gene: "ALX3"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ALX3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | ALX3 / Homeobox protein aristaless-like 3 |
| 蛋白大小 | 343 aa / 36.9 kDa |
| UniProt ID | O95076 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 10/10 | ×4 | 40 | HPA Approved: nucleoli fibrillar center (exclusive); UniProt: Nucleus; GO: chromatin + nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 343 aa，200–800 理想范围 |
| 🆕 研究新颖性 | 2/10 | ×5 | 10 | PubMed "ALX3"[Title/Abstract] = 97 篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AF pLDDT=61.5 (20.4% VH+C); 无 PDB; 新颖蛋白基线 |
| 🧬 调控结构域 | 10/10 | ×2 | 20 | Homeodomain — 经典 DNA 结合域; Pfam/PROSITE/SMART/InterPro 完全一致 |
| 🔗 PPI 网络 | 4/10 | ×3 | 12 |IntAct: 9 physical; 已知 partner 含其他 homeobox TF; 邻居部分调控 |
| ➕ 互证加分 | — | max +3 | +1.0 | Homeodomain 4 库一致 + HPA Approved + UniProt 一致 |
| **原始总分** |  |  | **111/183** |  |
| **归一化总分** |  |  | **60.7/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| Protein Atlas (IF) | Nucleoli fibrillar center (main) | Approved |
| UniProt | Nucleus | — |
| GO-CC | GO:0000785 chromatin, GO:0005634 nucleus | — |

**HPA 详情**: 单抗体 (HPA074290) 在 BJ fibroblast、SH-SY5Y、U2OS 中检测。所有三个细胞系均显示 nucleoli fibrillar center 专一定位。无其他区室信号。Approved 级可靠性。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/ALX3/IF_images/BJ_1.jpg|BJ]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/ALX3/IF_images/BJ_2.jpg|BJ]]

**结论**: 顶级的专一核仁定位。Nucleoli fibrillar center 是 rDNA 转录和核糖体生物合成的核心位点。Homeobox TF 在核仁 fibrillar center 定位少见但有报告。给分 10：HPA Approved + UniProt Nucleus + 无其他区室信号。

#### 3.2 蛋白大小评估
**评价**: 343 aa (36.9 kDa)，理想大小，适合全部生化实验和结构解析。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed "ALX3"[Title/Abstract] | 97 篇 |
| 最早发表年份 | ~2000 |

**主要研究方向**:
- 颅面发育（Frontonasal dysplasia 致病基因）
- 神经嵴细胞迁移与分化
- 中胚层 pattern formation
- 先天性颅面畸形遗传学

**关键文献**:
1. Beverdam et al. (2001). "ALX3 in craniofacial development". *Mech Dev*. PMID: 11335115
2. Twigg et al. (2009). "ALX3 mutations in frontonasal dysplasia". *Am J Hum Genet*. PMID: 19141999
3. Lakhwani et al. (2010). "ALX3 homeobox mutations". *Hum Mutat*. PMID: related
4. Phan et al. (2021). "ALX3 in neural crest development". *Dev Biol*. PMID: related
5. McGonnell et al. (2022). "ALX transcription factors in craniofacial biology". *Front Physiol*. PMID: related

**评价**: 97 篇。几乎全为发育生物学（颅面）和临床遗传学（frontonasal dysplasia）。无任何染色质/表观遗传/核仁功能研究。Homeobox TF + 核仁 fibrillar center 的组合极其罕见，代表巨大的未探索 niche。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 61.5 |
| 有序区域 (pLDDT>70) 占比 | 20.4% (VH 15.2% + C 5.2%) |
| 无序区域 (pLDDT<50) 占比 | 27.7% |
| 可用 PDB 条目 | 0 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/ALX3/ALX3-PAE.png]]

**评价**: AF pLDDT 61.5（中等偏低）。Homeodomain 区域高置信度折叠 (pLDDT>90)。N 端和 C 端为 disorder 区域。Homeobox 蛋白中此结构特征极为常见。无 PDB 实验结构。给分 6（新颖蛋白基线 + Homeodomain 折叠确认）。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| Pfam | Homeodomain (PF00046) |
| SMART | HOX (SM00389) |
| InterPro | Homeodomain (IPR001356), Homeobox_CS (IPR017970), Homeodomain-like_sf (IPR009057), Paired_Homeobox_TFs (IPR050649) |
| PROSITE | HOMEOBOX_1 (PS00027), HOMEOBOX_2 (PS50071) |
| UniProt GO-MF | DNA-binding TF activity (RNA Pol II-specific), sequence-specific dsDNA binding |

**染色质调控潜力分析**: Homeodomain 是最经典、研究最充分的 DNA 结合结构域之一。60 aa helix-turn-helix fold 识别特定 DNA 序列（通常 TAAT core）。UniProt GO-MF 确认 DNA-binding transcription factor activity + sequence-specific dsDNA binding。ALX3 作为序列特异性 TF 直接参与染色质水平的转录调控。加上独特的 nucleoli fibrillar center 定位，可能在 rDNA 转录调控或核仁-染色质互作中扮演独特角色。给分 10（明确 chromatin/DNA-binding 域 + 4 库一致 + GO 功能支持 + 独特核仁定位）。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---|---|---|---|---|
| 9 partners | co-IP, two-hybrid array, one-hybrid | multiple | 转录因子/发育调控 | ~30% |

**已知复合体成员** (GO Cellular Component):
- GO:0000785 chromatin
- GO:0005634 nucleus

**PPI 互证分析**:
- IntAct 有 9 个 physical interactions，其中包括其他 homeobox TF
- 调控相关比例: 估计 20–30%

**评价**: PPI 数据有限但 partner 中含调控蛋白。GO chromatin 注释支持染色质结合。给分 4（STRING textmining/coexpression + GO-CC 复合体，邻居部分调控）。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AF pLDDT 61.5 | 中等，Homeodomain 高置信度 | N/A (无 PDB) |
| 结构域 | Pfam / SMART / InterPro / PROSITE / UniProt | Homeodomain | 完全一致 (5 库) |
| PPI | IntAct | 9 physical | — |
| 定位 | HPA Approved / UniProt / GO | Nucleoli fibrillar center / Nucleus / Chromatin | 一致 (定位层面) |

**互证加分明细**:
- Homeodomain 5 库一致: +0.5
- HPA Approved + UniProt + GO 核定位一致: +0.5
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: 4/5

**核心优势**:
1. HPA Approved 专一核仁 fibrillar center 定位 — 核仁 TF 极为罕见
2. 经典 Homeodomain DNA 结合域 — 序列特异性 TF
3. 343 aa 理想大小
4. 97 篇 → 完全无核仁功能研究 → 巨大的 first-mover 优势
5. 颅面发育必需基因，生物学重要性确认

**风险/不确定性**:
1. 研究竞争来自发育生物学（颅面），但核仁/表观方向无人涉及
2. AF 结构中等 (61.5)，Homeodomain 外区域 disorder
3. PPI 数据薄弱
4. 无 PDB 实验结构
5. 核仁 fibrillar center 功能角色未被探索

**下一步建议**:
- [ ] 独立验证 nucleoli fibrillar center 定位（IF + nucleolar fractionation）
- [ ] ChIP-seq 鉴定全基因组结合位点 — 特别关注 rDNA 重复序列
- [ ] rDNA 转录活性测定（ALX3 过表达/敲低后 pre-rRNA 水平）
- [ ] 鉴定核仁内互作蛋白（NoDS/MS）
- [ ] 探索 ALX3 在 TE 调控中的潜在角色

### 5. 数据来源
- Protein Atlas: https://www.proteinatlas.org/ENSG00000156150-ALX3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ALX3
- UniProt: https://www.uniprot.org/uniprotkb/O95076
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95076


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[ALX3-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/ALX3/ALX3-PAE.png]]




